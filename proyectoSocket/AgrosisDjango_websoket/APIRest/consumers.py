from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ObjectConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Agrega este consumidor al grupo "objects_group"
        await self.channel_layer.group_add(
            "objects_group",
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Elimina este consumidor del grupo "objects_group"
        await self.channel_layer.group_discard(
            "objects_group",
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Envía el mensaje de vuelta al cliente
        await self.send(text_data=json.dumps({
            'message': message
        }))

    async def nuevo_objeto(self, event):
        # Maneja el evento "nuevo_objeto" enviado al grupo
        message = event['message']

        # Envía el mensaje de vuelta al cliente
        await self.send(text_data=json.dumps({
            'message': message
        }))
