import json
import asyncio

from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer

from chat.models import Message

User = get_user_model()


class ChatConsumer(WebsocketConsumer):
    def fetch_messages(self, data):
        messages = Message.last_10_messages()
        self.send_message(
            {"command": "messages", "messages": self.messages_to_json(messages)}
        )

    def new_message(self, data):
        author = data["from"]
        author_user = User.objects.filter(username=author)[0]
        message = Message.objects.create(author=author_user, content=data["message"])
        return self.send_chat_message(
            {"command": "new_message", "message": self.message_to_json(message)}
        )

    def messages_to_json(self, messages):
        """
        this method returns a list comprehension of messages, to json representation.
        The enumeration in this list comprehension is to create unique keys for the message,
        this will prevent sending actual message id to the public interface.
        """
        return [self.message_to_json(message) for message in messages]

    def message_to_json(self, message):
        _id = message.id
        author = message.author.username
        content = message.content
        profile_image = message.author.profile.image.url
        timestamp = str(message.timestamp)
        return {
            "id": _id,
            "author": author,
            "content": content,
            "profile_image": profile_image,
            "timestamp": timestamp,
        }

    commands = {
        "ping": "pong",
        "marco": "polo",
        "hello": "Hello World!",
        "foo": "bar",
        "fetch_messages": fetch_messages,
        "new_message": new_message,
    }

    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name.replace(' ', '_')}"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        utc_time = datetime.datetime.now(datetime.timezone.utc).isoformat()
        self.commands.get(data["command"])(self, data)

    def send_chat_message(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "utc_time": utc_time,
            },
        )

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    def chat_message(self, event):
        message = event["message"]
        utc_time = event["utc_time"]
        self.send(text_data=json.dumps(message))
