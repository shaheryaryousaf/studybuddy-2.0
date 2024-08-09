from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (
    LoginView, PasswordChangeView, PasswordChangeDoneView, LogoutView)

urlpatterns = [
    path('signup', views.signUp, name="signup"),
    path('signin', auth_views.LoginView.as_view(
        redirect_authenticated_user=True), name='signin'),
    path("logout", LogoutView.as_view(), name='logout'),
    path('profile/<str:id>', views.userProfile, name="profile"),
    path('update-profile', views.updateProfile, name="update-profile"),
    path('update-password', PasswordChangeView.as_view(), name="update-password"),
    path('password_change_done', PasswordChangeDoneView.as_view(),
         name="password_change_done"),
]
