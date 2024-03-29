import datetime
import logging

from kafka_common.receiver import SingletonMixin
from repository.courier_repository import CourierRepository
from repository.delivery_repository import DeliveryRepository
from schemas.schemas import Delivery, Location
from utils import DistanceCalculator


class NotificationService(SingletonMixin):

    def __init__(self):
        self.delivery_repository = DeliveryRepository()
        self.courier_repository = CourierRepository()

    async def distribute_notifications(self) -> list[Delivery]:
        not_picked_up_deliveries = await self.delivery_repository.get_by_kwargs(status=3)
        picked_up_deliveries = await self.delivery_repository.get_by_kwargs(status=4)

        to_notify_list = []
        for delivery in not_picked_up_deliveries + picked_up_deliveries:
            in_time = await self.check_delivery_timing(delivery)
            if not in_time:
                if not delivery.last_notification_ts or (
                        datetime.datetime.now() - delivery.last_notification_ts) >= datetime.timedelta(minutes=2):
                    delivery.last_notification_ts = datetime.datetime.now()
                    to_notify_list.append(delivery)

        return to_notify_list

    async def check_delivery_timing(self, delivery: Delivery):
        courier = await self.courier_repository.get(delivery.courier)
        points = []
        if delivery.status == 3:
            points.append(Location(delivery.latitude, delivery.longitude))

        points.append(Location(delivery.consumer_latitude, delivery.consumer_longitude))

        calculator = DistanceCalculator()
        left_distance = await calculator.get_left_distance_between_many_points(courier.location, *points)
        left_distance_requiring_time = left_distance / calculator.avg_courier_speed

        in_time = await self.compare_actual_time_and_estimated_time(left_distance_requiring_time,
                                                                    delivery.estimated_time)
        logging.warning(f'GOT IN TIME {in_time} FOR DELIVERY {delivery}')
        return in_time

    async def compare_actual_time_and_estimated_time(self, left_time: float, estimated_time: datetime.datetime) -> bool:
        return datetime.timedelta(hours=left_time) + datetime.datetime.now() <= estimated_time
