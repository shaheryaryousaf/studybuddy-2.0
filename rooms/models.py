from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


# ===============================
# Category Models
# ===============================
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# ===============================
# Room Models
# ===============================
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(
        User, related_name='participants', null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# ===============================
# Message Models
# ===============================
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
