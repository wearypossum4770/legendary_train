from crispy_forms.helper import FormHelper
from django.contrib.auth import get_user_model
from django.forms import ModelForm, EmailField
from django.contrib.auth.forms import UserCreationForm

from users.models import Profile

User = get_user_model()


class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    email = EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    email = EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]


class FriendForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)


class ProfileUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:
        model = Profile
        fields = ["image"]
