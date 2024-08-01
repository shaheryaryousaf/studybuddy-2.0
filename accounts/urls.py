from django.urls import path
from . import views

urlpatterns = [
    path('sign-in', views.signIn, name="sign-in"),
    path('sign-up', views.signUp, name="sign-up"),
    path('profile', views.userProfile, name="profile"),
    path('update-profile', views.updateProfile, name="update-profile"),
]