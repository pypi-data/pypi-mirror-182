from typing import Any, Callable, List, Optional

from returns.curry import partial
from returns.functions import tap
from returns.future import FutureFailure, FutureResult, FutureSuccess
from returns.iterables import Fold
from returns.maybe import Maybe
from returns.pipeline import flow, managed, pipe
from returns.pointfree import bind, map_
from returns.result import Result, Success
from src.modules.ai_market.infrastructure.config import (broker_host,
                                                         broker_port,
                                                         broker_user_name,
                                                         broker_user_password,
                                                         broker_virtual_host,
                                                         get_posgres_uri)

from dino_seedwork_be.adapters.messaging.rabbitmq.ConnectionSettings import \
    ConnectionSettings
from dino_seedwork_be.adapters.messaging.rabbitmq.Exchange import Exchange
from dino_seedwork_be.adapters.messaging.rabbitmq.MessageParameters import \
    MessageParameters
from dino_seedwork_be.adapters.messaging.rabbitmq.MessageProducer import \
    MessageProducer
from dino_seedwork_be.event.EventSerializer import EventSerializer
from dino_seedwork_be.event.EventStore import EventStore
from dino_seedwork_be.event.StoredEvent import StoredEvent
from dino_seedwork_be.exceptions import MainException
from dino_seedwork_be.pubsub.Notification import Notification
from dino_seedwork_be.pubsub.NotificationPublisher import NotificationPublisher
from dino_seedwork_be.pubsub.NotificationSerializer import \
    NotificationSerializer
from dino_seedwork_be.pubsub.PublishedNotificationTrackerStore import \
    PublishedNotificationTrackerStore
from dino_seedwork_be.storage.uow import SuperDBSessionUser
from dino_seedwork_be.utils.functional import (feedArgs, feedKwargs,
                                               print_result_with_text,
                                               return_v)


class RabbitMQPublisher(NotificationPublisher, SuperDBSessionUser):
    _event_store: EventStore
    _exchange_name: str
    _published_notif_tracker_store: PublishedNotificationTrackerStore
    _message_producer_ins: Optional[MessageProducer] = None
    _event_serializer: EventSerializer

    def __init__(
        self,
        event_store: EventStore,
        exchange_name: str,
        published_notif_tracker_store: PublishedNotificationTrackerStore,
        event_serializer: EventSerializer,
        session_factory: Callable,
    ) -> None:
        # session = session_factory()
        self.set_exchange_name(exchange_name)
        self.set_event_store(event_store)
        # self._event_store.set_session(session)
        self._message_producer()
        self.set_published_notif_tracker_store(published_notif_tracker_store)
        # self._published_notif_tracker_store.set_session(session)
        self.set_session_users(
            [self.event_store(), self.published_notif_tracker_store()]
        )
        self._event_serializer = event_serializer
        super().__init__()

    def event_serializer(self):
        return self._event_serializer

    def publish_notifications(self) -> FutureResult[Maybe[int], Any]:
        """
        publish unpublished event in event store
        :return: return the last event int id that published already
        """

        def notifications_from(
            events: List[StoredEvent],
        ) -> Result[List[Notification], Any]:
            return flow(
                events,
                partial(
                    map,
                    lambda stored_event: flow(
                        None,
                        lambda _: self.event_serializer().deserialize(
                            stored_event.body()
                        ),
                        map_(
                            lambda domain_event: list(
                                [
                                    stored_event.id().value_or(None),
                                    domain_event,
                                ]
                            )
                        ),
                        bind(feedArgs(Notification.factory)),
                    ),
                ),
                list,
                lambda results: Fold.collect(results, Success(())),
            )

        def publish_future(
            msg_producer: MessageProducer,
        ) -> FutureResult[Maybe[int], Any]:
            match msg_producer.is_ready_for_publish():
                case False:
                    return FutureFailure(MainException("MessageProducer not ready yet"))
                case True:
                    return (
                        self.published_notif_tracker_store()
                        .published_notification_tracker()
                        .bind(
                            lambda tracker: flow(
                                tracker.most_recent_published_notification_id().value_or(
                                    0
                                ),
                                self.event_store().all_stored_events_since,
                                bind(
                                    pipe(notifications_from, FutureResult.from_result)
                                ),
                                map_(
                                    print_result_with_text("notification from results")
                                ),
                                bind(
                                    pipe(
                                        partial(
                                            map,
                                            lambda notif: flow(
                                                notif,
                                                partial(self._publish, msg_producer),
                                                map_(return_v(notif)),
                                            ),
                                        ),
                                        lambda publish_results: Fold.collect(
                                            publish_results, FutureSuccess(())
                                        ),
                                    )
                                ),
                                bind(
                                    partial(
                                        self.published_notif_tracker_store().track_most_recent_published_notification,
                                        tracker,
                                    )
                                ),
                            )
                        )
                    )

        def close_producer(producer: MessageProducer, _):
            producer.close()
            return FutureSuccess(None)

        return managed(publish_future, close_producer)(
            FutureResult.from_result(self._message_producer())
        )

    def _publish(
        self,
        a_message_producer: MessageProducer,
        a_notification: Notification,
    ) -> FutureResult[None, Exception]:
        return flow(
            {
                "a_type": a_notification.type_name(),
                "a_message_id": str(a_notification.id()),
                "a_timestamp": int(a_notification.occurred_on().timestamp()),
            },
            feedKwargs(MessageParameters.durable_text_parameters),
            lambda text_parameters: flow(
                a_notification,
                NotificationSerializer.instance().serialize,
                map_(tap(print_result_with_text("notification serialized"))),
                bind(
                    lambda notif: FutureResult.from_result(
                        a_message_producer.send(text_parameters, notif)
                    )
                ),
            ),
        )

    def event_store(self) -> EventStore:
        return self._event_store

    def exchange_name(self) -> str:
        return self._exchange_name

    def published_notif_tracker_store(self) -> PublishedNotificationTrackerStore:
        return self._published_notif_tracker_store

    def set_event_store(self, event_store: EventStore):
        self._event_store = event_store

    def set_exchange_name(self, a_name: str):
        self._exchange_name = a_name

    def _set_message_producer(self, message_producer: MessageProducer):
        self._message_producer_ins = message_producer

    def _message_producer(self) -> Result[MessageProducer, Any]:
        match self._message_producer_ins:
            case None:
                return flow(
                    [
                        ConnectionSettings.factory(
                            broker_host(),
                            broker_port(),
                            broker_virtual_host(),
                            broker_user_name().value_or(None),
                            broker_user_password().value_or(None),
                        ),
                        self.exchange_name(),
                        True,
                    ],
                    feedArgs(Exchange.fanout_instance),
                    map_(MessageProducer.factory),
                    map_(tap(self._set_message_producer)),
                )
            case MessageProducer():
                return Success(self._message_producer_ins)
            case _:
                print("not message producer in case", self._message_producer_ins)

    def set_published_notif_tracker_store(
        self, a_published_notif_tracker_store: PublishedNotificationTrackerStore
    ):
        self._published_notif_tracker_store = a_published_notif_tracker_store

    def run(self):
        self._message_producer().unwrap().run()

    def is_ready(self) -> Result[bool, Any]:
        return (
            self._message_producer()
            .map(lambda producer: producer.is_ready_for_publish())
            .lash(lambda _: Success(False))
        )

    def get_last_published_notification_id(self) -> FutureResult[Maybe[int], Any]:
        return (
            self.published_notif_tracker_store()
            .published_notification_tracker()
            .map(lambda tracker: tracker.most_recent_published_notification_id())
        )
