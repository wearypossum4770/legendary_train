from django.contrib.auth.models import User
from django.contrib.admin import StackedInline, site
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import Profile


class ProfileInline(StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_select_related = ("profile",)
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "get_location",
    )

    def get_location(self, instance):
        return instance.profile.location

    get_location.short_description = "Location"

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super().get_inline_instances(request, obj)


site.unregister(User)
site.register(User, UserAdmin)
