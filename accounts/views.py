from django.shortcuts import render, redirect
from .forms import UserModelForm, ProfileCreateForm
from django.contrib.auth import get_user_model
User = get_user_model()


# Signup
def signUp(request):
    form = UserModelForm()
    if request.method == "POST":
        form = UserModelForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.type = "user"
            f.save()
            return redirect('signin')
    context = {
        'form': form
    }
    return render(request, 'registration/signup.html', context)


# Profile
def userProfile(request):
    user = User.objects.get(id=request.user.id)
    rooms = user.room_set.all()
    context = {
        'rooms': rooms
    }
    return render(request, 'accounts/profile.html', context)


# Update Profile
def updateProfile(request):
    form = ProfileCreateForm(instance=request.user.profile)
    if request.method == "POST":
        form = ProfileCreateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('/account/update-profile')

    context = {
        'form': form
    }
    return render(request, 'accounts/update-profile.html', context)
