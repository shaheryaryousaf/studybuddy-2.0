from django.shortcuts import render, redirect
from .forms import UserModelForm


# Signup
def signUp(request):
    form = UserModelForm()
    if request.method == "POST":
        form = UserModelForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.type="user"
            f.save()
            return redirect('signin')
    context = {
        'form': form
    }
    return render(request, 'registration/signup.html', context)


# Profile
def userProfile(request):
    return render(request, 'accounts/profile.html')


# Update Profile
def updateProfile(request):
    return render(request, 'accounts/update-profile.html')
