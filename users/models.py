from django.contrib.auth import get_user_model
from django.db.models import (
    CASCADE,
    CharField,
    DateTimeField,
    ForeignKey,
    ImageField,
    ManyToManyField,
    Model,
    OneToOneField,
    TextField,
)
from django.utils import timezone
from PIL import Image

User = get_user_model()
# https://github.com/revsys/django-friendship/blob/master/friendship/models.py
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


#     def accept(self):
#         """ Accept this friendship request """
#         Friend.objects.create(from_user=self.from_user, to_user=self.to_user)
#         Friend.objects.create(from_user=self.to_user, to_user=self.from_user)
#         friendship_request_accepted.send(
#             sender=self, from_user=self.from_user, to_user=self.to_user
#         )
#         self.delete()
#         # Delete any reverse requests
#         FriendshipRequest.objects.filter(
#             from_user=self.to_user, to_user=self.from_user
#         ).delete()

#         # Bust requests cache - request is deleted
#         # bust_cache("requests", self.to_user.pk)
#         # bust_cache("sent_requests", self.from_user.pk)
#         # Bust reverse requests cache - reverse request might be deleted
#         # bust_cache("requests", self.from_user.pk)
#         # bust_cache("sent_requests", self.to_user.pk)
#         # Bust friends cache - new friends added
#         # bust_cache("friends", self.to_user.pk)
#         # bust_cache("friends", self.from_user.pk)
#         return True

#     def reject(self):
#         """ reject this friendship request """
#         self.rejected = timezone.now()
#         self.save()
#         friendship_request_rejected.send(sender=self)
#         # bust_cache("requests", self.to_user.pk)
#         return True

#     def cancel(self):
#         """ cancel this friendship request """
#         self.delete()
#         friendship_request_canceled.send(sender=self)
#         # bust_cache("requests", self.to_user.pk)
#         # bust_cache("sent_requests", self.from_user.pk)
#         return True

#     def mark_viewed(self):
#         self.viewed = timezone.now()
#         friendship_request_viewed.send(sender=self)
#         self.save()
#         # bust_cache("requests", self.to_user.pk)
#         return True
def upload_file():
    profiles = Profile.objects.all()


output_size = (300, 300)


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    middle_name = CharField(max_length=50, null=True, blank=True)
    friends = ManyToManyField(User, blank=True, related_name="friends")
    image = ImageField(default="default.webp", upload_to="profile_pics")
    headline = CharField(max_length=50, null=True, blank=True)
    bio = TextField(null=True, blank=True)

    @property
    def process_image(self):
        return [self.user, self.image]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        print(self.image.__dict__)
        return f"{self.user.first_name.capitalize()} {self.user.last_name.capitalize()}'s  Profile"
