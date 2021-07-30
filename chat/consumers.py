import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .views import respond_to_websockets

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        payload = json.loads(text_data)
        command = payload.pop('command', 'invalid.command')
        handler_name = f"chat.{command}"

        async_to_sync(self.channel_layer.send)(self.channel_name, {
            'type': handler_name,
            'payload': payload
            })
    
    def chat_start(self, event):
        pass

    def chat_send(self, event):
        message = event['payload']
        user = self.scope['user']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'type': 'text',
            'text': message['text'],
            'source': 'CANDIDATE'
        }))
        response = respond_to_websockets(message, user)

        response['source'] = 'BOT'
        self.send(text_data=json.dumps(response))

    def chat_leave(self, event):
        pass

    def chat_invalid_command(self, message):
        self.send(text_data=json.dumps({
            'type': 'text',
            'text': 'invalid command',
            'source': 'CANDIDATE'
        }))