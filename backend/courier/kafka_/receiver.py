import json

from bot.kafka_common.receiver import KafkaReceiver
from courier.kafka_.sender import send_courier_profile_from_django_to_telegram
from utils.location_tracker import LocationTracker


class CourierLocationReceiver(KafkaReceiver):
    _topic = 'courier_location'

    def __init__(self):
        super().__init__()
        self.location_tracker = LocationTracker()
        
    def post_consume_action(self, msg: str):
        msg_dict = json.loads(msg)
        self.location_tracker.set_location(courier_id=msg_dict['courier_id'], location=msg_dict['location'])


class CourierProfileAskReceiver(KafkaReceiver):
    _topic = 'ask_courier_profile'

    def post_consume_action(self, msg: str):
        msg = json.loads(msg)
        send_courier_profile_from_django_to_telegram(msg)
