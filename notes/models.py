from django.utils.translation import gettext_lazy as _
from django.db.models import (
    Model,
    URLField,
    CharField,
    JSONField,
    TextField,
    TextChoices,
    DateTimeField,
    OneToOneField,
)


class Note(Model):
    """
    This is a fake google keep, so I named it  keep-fake,
    Kind of like keep safe, but fake.
    """

    class Status(TextChoices):
        ARCHIVED = "A", _("Archive Note")
        DELETED = "D", _("Note is soft deleted")
        UNREAD = "U", _("Unread Note")

    title = CharField(max_length=70, null=True, blank=True)
    note_body = TextField(null=True, blank=True)
    date_created = DateTimeField(auto_now_add=True, null=True, blank=True)
    date_modified = DateTimeField(auto_now=True, null=True, blank=True)
    date_published = DateTimeField(auto_now=True, null=True, blank=True)
    status = CharField(max_length=1, choices=Status.choices, null=True, blank=True)
    keywords = CharField(max_length=200, default=str, null=True, blank=True)
    mentions = JSONField(default=dict, null=True, blank=True)
    thumbnail_url = URLField(null=True, blank=True)
