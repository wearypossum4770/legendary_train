from PIL import Image
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.db.models import (
    CASCADE,
    Model,
    CharField,
    DateField,
    TextField,
    ForeignKey,
    ImageField,
    TextChoices,
    BooleanField,
    DateTimeField,
    OneToOneField,
    ManyToManyField,
)

User = get_user_model()


class Profile(Model):
    class Pronouns(TextChoices):
        HE = "H", _("He/Him His, Himself")
        SHE = "S", _("She/Her Hers, Herself")
        THEY = "T", _("They/Them Theirs, themself")
        ZE = "Z", _("Ze (or Zie or Xe)	Zee (like “see” with a “Z”)")

    has_leads = BooleanField(default=False)
    has_tasks = BooleanField(default=True)
    has_notes = BooleanField(default=True)
    has_chat = BooleanField(default=True)
    is_student = BooleanField(default=False)
    is_teacher = BooleanField(default=False)
    user = OneToOneField(User, on_delete=CASCADE)
    location = CharField(max_length=20, blank=True, null=True)
    middle_name = CharField(max_length=50, null=True, blank=True)
    pronouns = CharField(max_length=1, choices=Pronouns.choices, default=Pronouns.THEY)
    friends = ManyToManyField(User, blank=True, related_name="friends")
    birthdate = DateField(null=True, blank=True)
    image = ImageField(default="default.webp", upload_to="profile_pics")
    headline = CharField(max_length=50, null=True, blank=True)
    bio = TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name.capitalize()} {self.user.last_name.capitalize()}'s  Profile"


class FriendRequest(Model):
    """Model to represent friendship requests"""

    from_user = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name="friend_req_sent",
    )
    to_user = ForeignKey(
        User,
        on_delete=CASCADE,
        related_name="friend_req_received",
    )
    message = TextField(blank=True)
    created = DateTimeField(default=timezone.now)
    rejected = DateTimeField(blank=True, null=True)
    viewed = DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = ("from_user", "to_user")

    def __str__(self):
        return f"{self.from_user_id}"
