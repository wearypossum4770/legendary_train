<<<<<<< HEAD
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.api.rest_views import ProfileViewSet, UserViewSet
from users.views import  profile, register
=======
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

from users.api.rest_views import UserViewSet, ProfileViewSet
from users.views import profile, register, find_users_friends
>>>>>>> 07b0ff3d47923f9eeeb106dff01ed70b8cf689f5

router = DefaultRouter()
# app_name = "users"
router.register(r"users", UserViewSet)
router.register(r"profile", ProfileViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
<<<<<<< HEAD
    # path("friends/", find_users_friends, name="friends"),
    # path("send_freind_request/<int:userId/"),
    # path("accept_friend_request/<int:requestId/"),
    # path("register/", register, name="register"),
=======
    path("friends/", find_users_friends, name="friends"),
    # path("send_freind_request/<int:userId/"),
    # path("accept_friend_request/<int:requestId/"),
    path("register/", register, name="register"),
>>>>>>> 07b0ff3d47923f9eeeb106dff01ed70b8cf689f5
    path("profile/", profile, name="profile"),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path(
        "logout/", LogoutView.as_view(template_name="users/logout.html"), name="logout"
    ),
    path(
        "password-reset/",
        PasswordResetView.as_view(template_name="users/password_reset.html"),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
