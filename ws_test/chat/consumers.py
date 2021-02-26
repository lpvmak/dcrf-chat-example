from djangochannelsrestframework.consumers import AsyncAPIConsumer
from djangochannelsrestframework.observer import model_observer

from chat.models import Message
from chat.serializers import MessageSerializer


class ChatConsumer(AsyncAPIConsumer):
    async def accept(self, subprotocol=None):
        await super().accept()
        await self.message_change_handler.subscribe()

    def receive(self, text_data=None, bytes_data=None, **kwargs):
        pass

    @model_observer(Message)
    async def message_change_handler(self, message, observer=None, action=None, **kwargs):
        await self.send_json(dict(status=200, body=message, action=action))

    @message_change_handler.groups_for_signal
    def message_change_handler_groups_for_signal(self, instance, **kwargs):
        yield f'-chat'

    @message_change_handler.serializer
    def model_serialize(self, instance, action, **kwargs):
        return MessageSerializer(instance).data

    @message_change_handler.groups_for_consumer
    def message_change_handler_groups_for_consumer(self, **kwargs):
        yield f'-chat'
