from django.urls import path
from . import views

urlpatterns = [
    path('create', views.createRoom, name="create-room"),
    path('<str:id>', views.singleRoom, name="single-room")
]
