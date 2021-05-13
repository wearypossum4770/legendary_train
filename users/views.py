from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.authentication import (
    BasicAuthentication,
    TokenAuthentication,
    SessionAuthentication,
)

from users.models import Profile, FriendRequest
from users.forms import UserUpdateForm, UserRegisterForm, ProfileUpdateForm

User = get_user_model()


@api_view(["GET", "POST"])
@authentication_classes(
    [SessionAuthentication, BasicAuthentication, TokenAuthentication]
)
@permission_classes([IsAuthenticated, IsAdminUser])
def commander(request, format=None):
    print(request)
    content = {
        "user": str(request.user),  # `django.contrib.auth.User` instance.
        "auth": str(request.auth),  # None
    }
    return JsonResponse(content)


@login_required
def send_friend_request(request):

    from_user = request.user
    to_user = User.objects.get(id=request.user.id)
    friend_request, created = FriendRequest.objects.get_or_create(
        from_user=from_user, to_user=to_user
    )
    if created:
        return HttpResponse("freind request sent")
    else:
        return HttpResponse("friend request was already sent")


# @login_required
# def load_all_users(request):
@login_required
def find_users_friends(request):
    friend_list = Profile.objects.get(user=request.user).friends.all()
    one = friend_list[0]
    print("\n\n\n")
    print(one.profile.image)
    # print(friends.__dict__)
    return render(request, "users/friends.html", {"friend_list": friend_list})


# @login_required
# def filter_users_not_connected(request):


@login_required
def accept_friend_request(request, request_id):
    friend_request = FriendRequest.objects.get(id=request_id)
    if friend_request.to_user == request.user:
        friend_request.to_user.freinds.add(friend_request.from_user)
        friend_request.from_user.freinds.add(friend_request.to_user)
        friend_request.delete()
        return HttpResponse("friend request accepted")
    else:
        return HttpResponse("friend request not accepted")


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Your account has been created! You are now able to log in"
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, "users/profile.html", {"u_form": u_form, "p_form": p_form})


def validate_form(form, *args, **kwargs):
    ...


def create_profile(request):
    ...


def edit_profile(request, user_id):
    ...
