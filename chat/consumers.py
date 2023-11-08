import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from .models import Message, DirectMessage


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from web socket
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']

        await self.save_message(username, room, message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {'type': 'chat_message', 'message': message, 'username': username},
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        username = event['username']

        # Send message to WebSocket
        await self.send(
            text_data=json.dumps({'message': message, 'username': username})
        )

    @sync_to_async
    def save_message(self, username, room, message):
        Message.objects.create(username=username, room=room, content=message)


class ChatDmConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_dm_%s' % self.room_name

        # Join room
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from web socket
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        senderUsername = data['senderUsername']
        receiverUsername = data['receiverUsername']
        room = data['room']

        await self.save_message(senderUsername, receiverUsername, room, message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'senderUsername': senderUsername,
                'receiverUsername': receiverUsername,
            },
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        senderUsername = event['senderUsername']
        receiverUsername = event['receiverUsername']

        # Send message to WebSocket
        await self.send(
            text_data=json.dumps(
                {
                    'message': message,
                    'senderUsername': senderUsername,
                    'receiverUsername': receiverUsername,
                }
            )
        )

    @sync_to_async
    def save_message(self, senderUsername, receiverUsername, room, message):
        DirectMessage.objects.create(
            sender=senderUsername, receiver=receiverUsername, room=room, content=message
        )