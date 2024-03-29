from bot.kafka_common.receiver import SingletonMixin
from bot.kafka_common.sender import KafkaSender
from delivery.models import Delivery
from django.core.serializers import serialize


def send_delivery_to_tg(delivery_orm: Delivery):
    serialized_delivery = serialize('json', [delivery_orm])
    producer = DjangoDeliverySender()
    producer.send(serialized_delivery)


class DjangoDeliverySender(KafkaSender, SingletonMixin):
    _topic = 'to_deliver'
