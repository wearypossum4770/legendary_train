from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from users.models import Profile

User = get_user_model()


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "date_created",
            "date_modified",
            "image",
            "nickname",
            "phone_number",
            "user_metadata",
        ]


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username"]
