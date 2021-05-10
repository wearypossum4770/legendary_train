from uuid import uuid4
from pathlib import Path
from datetime import date

from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db.models import (
    CASCADE,
    Model,
    CharField,
    DateField,
    TextField,
    ForeignKey,
    TextChoices,
    BooleanField,
    DateTimeField,
)

User = get_user_model()


class Todo(Model):
    title = CharField(max_length=80)
    content = CharField(max_length=100)
    date_modified = DateTimeField(auto_now=True)
    date_created = DateTimeField(auto_now_add=True)
    date_due = DateField(null=True, blank=True)
    date_completed = DateTimeField(null=True, blank=True)
    completed = BooleanField(default=False)
    created_by = ForeignKey(
        User,
        related_name="todo_created_by",
        null=True,
        blank=True,
        on_delete=CASCADE,
    )
    assigned_to = ForeignKey(
        User,
        related_name="todo_assigned_to",
        blank=True,
        null=True,
        on_delete=CASCADE,
    )
    note = TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        if self.completed:
            self.date_completed = timezone.now()
        super().save()

    @property
    def is_due(self, *args, **kwargs):
        return date.today() == self.date_due

    @property
    def is_overdue(self, *args, **kwargs):
        return date.today() > self.date_due
