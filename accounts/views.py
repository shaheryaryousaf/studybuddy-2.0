from django.shortcuts import render


# Signin
def signIn(request):
    return render(request, 'accounts/signin.html')


# Signup
def signUp(request):
    return render(request, 'accounts/signup.html')


# Profile
def userProfile(request):
    return render(request, 'accounts/profile.html')


# Update Profile
def updateProfile(request):
    return render(request, 'accounts/update-profile.html')
