#![warn(unsafe_op_in_unsafe_fn)]

use dora_core::{
    config::{CommunicationConfig, DataId, NodeId, OperatorId},
    descriptor::OperatorDefinition,
};
use dora_node_api::{
    self,
    communication::{self, CommunicationLayer, Publisher, STOP_TOPIC},
    manual_stop_publisher,
};
use eyre::{bail, Context, Result};
use futures::{Stream, StreamExt};
use operator::{spawn_operator, OperatorEvent, StopReason};

use std::{
    collections::{BTreeSet, HashMap},
    mem,
};
use tokio::{runtime::Builder, sync::mpsc};
use tokio_stream::{wrappers::ReceiverStream, StreamMap};

mod operator;

pub fn main() -> eyre::Result<()> {
    set_up_tracing().context("failed to set up tracing subscriber")?;

    let node_id: NodeId = {
        let raw =
            std::env::var("DORA_NODE_ID").wrap_err("env variable DORA_NODE_ID must be set")?;
        serde_yaml::from_str(&raw).context("failed to deserialize operator config")?
    };
    let communication_config: CommunicationConfig = {
        let raw = std::env::var("DORA_COMMUNICATION_CONFIG")
            .wrap_err("env variable DORA_COMMUNICATION_CONFIG must be set")?;
        serde_yaml::from_str(&raw).context("failed to deserialize communication config")?
    };
    let operators: Vec<OperatorDefinition> = {
        let raw =
            std::env::var("DORA_OPERATORS").wrap_err("env variable DORA_OPERATORS must be set")?;
        serde_yaml::from_str(&raw).context("failed to deserialize operator config")?
    };

    let mut communication: Box<dyn CommunicationLayer> =
        communication::init(&communication_config)?;

    let mut operator_events = StreamMap::new();
    let mut operator_stop_publishers = HashMap::new();
    let mut operator_events_tx = HashMap::new();

    for operator_config in &operators {
        let (events_tx, events) = mpsc::channel(1);
        let stop_publisher = publisher(
            &node_id,
            operator_config.id.clone(),
            STOP_TOPIC.to_owned().into(),
            communication.as_mut(),
        )
        .with_context(|| {
            format!(
                "failed to create stop publisher for operator {}",
                operator_config.id
            )
        })?;
        operator_stop_publishers.insert(operator_config.id.clone(), stop_publisher);

        operator_events.insert(operator_config.id.clone(), ReceiverStream::new(events));
        operator_events_tx.insert(operator_config.id.clone(), events_tx);
    }

    let operator_events = operator_events.map(|(id, event)| Event::Operator { id, event });
    let node_id_clone = node_id.clone();
    let tokio_runtime = Builder::new_current_thread()
        .enable_all()
        .build()
        .wrap_err("Could not build a tokio runtime.")?;
    let manual_stop_publisher = manual_stop_publisher(communication.as_mut())?;
    let stop_thread = std::thread::spawn(move || -> Result<()> {
        tokio_runtime.block_on(run(
            node_id_clone,
            operator_events,
            operator_stop_publishers,
            manual_stop_publisher,
        ))
    });

    for operator_config in &operators {
        let events_tx = operator_events_tx.get(&operator_config.id).unwrap();
        spawn_operator(
            &node_id,
            operator_config.clone(),
            events_tx.clone(),
            communication.as_mut(),
        )
        .wrap_err_with(|| format!("failed to init operator {}", operator_config.id))?;
    }

    stop_thread
        .join()
        .map_err(|err| eyre::eyre!("Stop thread failed with err: {err:#?}"))?
        .wrap_err("Stop loop thread failed unexpectedly.")?;
    Ok(())
}

async fn run(
    node_id: NodeId,
    mut events: impl Stream<Item = Event> + Unpin,
    mut operator_stop_publishers: HashMap<OperatorId, Box<dyn Publisher>>,
    manual_stop_publisher: Box<dyn Publisher>,
) -> eyre::Result<()> {
    #[cfg(feature = "metrics")]
    let _started = {
        use dora_metrics::init_meter;
        use opentelemetry::global;
        use opentelemetry_system_metrics::init_process_observer;

        let _started = init_meter();
        let meter = global::meter(Box::leak(node_id.to_string().into_boxed_str()));
        init_process_observer(meter);
        _started
    };

    let mut stopped_operators = BTreeSet::new();

    while let Some(event) = events.next().await {
        match event {
            Event::Operator { id, event } => {
                match event {
                    OperatorEvent::Error(err) => {
                        bail!(err.wrap_err(format!("operator {id} failed")))
                    }
                    OperatorEvent::Panic(payload) => std::panic::resume_unwind(payload),
                    OperatorEvent::Finished { reason } => {
                        if let StopReason::ExplicitStopAll = reason {
                            let hlc = dora_message::uhlc::HLC::default();
                            let metadata = dora_message::Metadata::new(hlc.new_timestamp());
                            let data = metadata
                                .serialize()
                                .wrap_err("failed to serialize stop message")?;
                            manual_stop_publisher
                                .publish(&data)
                                .map_err(|err| eyre::eyre!(err))
                                .wrap_err("failed to send stop message")?;
                            break;
                        }
                        if let Some(stop_publisher) = operator_stop_publishers.remove(&id) {
                            tracing::info!("operator {node_id}/{id} finished ({reason:?})");
                            stopped_operators.insert(id.clone());
                            // send stopped message
                            tokio::task::spawn_blocking(move || stop_publisher.publish(&[]))
                                .await
                                .wrap_err("failed to join stop publish task")?
                                .map_err(|err| eyre::eyre!(err))
                                .with_context(|| {
                                    format!(
                                        "failed to send stop message for operator `{node_id}/{id}`"
                                    )
                                })?;
                            if operator_stop_publishers.is_empty() {
                                break;
                            }
                        } else {
                            tracing::warn!("no stop publisher for {id}");
                        }
                    }
                }
            }
        }
    }

    mem::drop(events);

    Ok(())
}

fn publisher(
    self_id: &NodeId,
    operator_id: OperatorId,
    output_id: DataId,
    communication: &mut dyn CommunicationLayer,
) -> eyre::Result<Box<dyn Publisher>> {
    let topic = format!("{self_id}/{operator_id}/{output_id}");
    communication
        .publisher(&topic)
        .map_err(|err| eyre::eyre!(err))
        .wrap_err_with(|| format!("failed to create publisher for output {output_id}"))
}

enum Event {
    Operator {
        id: OperatorId,
        event: OperatorEvent,
    },
}

fn set_up_tracing() -> eyre::Result<()> {
    use tracing_subscriber::prelude::__tracing_subscriber_SubscriberExt;

    let stdout_log = tracing_subscriber::fmt::layer().pretty();
    let subscriber = tracing_subscriber::Registry::default().with(stdout_log);
    tracing::subscriber::set_global_default(subscriber)
        .context("failed to set tracing global subscriber")
}
