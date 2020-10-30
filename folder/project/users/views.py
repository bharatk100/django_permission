from django.shortcuts import render, HttpResponse, Http404, get_object_or_404, redirect
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ProfileFrom
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


"""
______________________Dashboard________________________
"""

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'users/dashboard.html', {'name': request.user.username})
    else:
        pass
    return render(request, 'users/dashboard.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_From = ProfileFrom(request.POST)

        if form.is_valid() and profile_From.is_valid():
            user = form.save()

            profile = profile_From.save(commit=False)
            profile.user = user
            profile.save()
            group = Group.objects.get(name='Editor') #here
            user.groups.add(group)
            messages.success(request, 'Your account has been  created. You can Log In')
            return redirect('login')

    else:
        form = UserRegisterForm()
        profile_From = ProfileFrom()
    return render(request, 'users/register.html', {'form': form, ' profile_From':  profile_From})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request, 'Your account has been  Updated..!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)


"""
______________________Logout________________________
"""


def logout_view(request):
    logout(request)

