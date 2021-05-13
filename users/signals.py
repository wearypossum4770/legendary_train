from django.dispatch import Signal, receiver
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from users.models import Profile


@receiver(post_save, sender=get_user_model, dispatch_uid="users.create_or_save_profile")
def create_or_save_profile(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
