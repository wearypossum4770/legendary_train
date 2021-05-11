from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from users.forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm
from users.models import Profile
@login_required
def profile_list(request):
    """
    List all public profiles 
    """ 
    profiles = Profile.objects.filter(is_active=True).order_by("last_name", "first_name")
    return render(request, 'users/profile_list.html', {"profiles":profiles})
@login_required
def profile(request):
    u_form = UserUpdateForm(request.POST, instance=request.user)
    p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
    print("\n\n\n\n\n\n\n")
    print((u_form, p_form,))
    
    if request.method == "POST":

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, "users/profile.html", {"u_form": u_form, "p_form": p_form})


def validate_form(form,*args,**kwargs):
    ...

def create_profile(request):
    ...
def edit_profile(request,user_id):
    ...
