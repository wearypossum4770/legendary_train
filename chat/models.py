from django.contrib.auth import get_user_model
from django.db.models import (
    CASCADE,
    Model,
    CharField,
    TextField,
    ForeignKey,
    DateTimeField,
)

User = get_user_model()


class Message(Model):
    author = ForeignKey(User, on_delete=CASCADE)
    content = TextField()
    timestamp = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_10_messages():
        return Message.objects.order_by("-timestamp").all()
