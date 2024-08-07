from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from .models import Profiles
from django.contrib.auth import get_user_model
User = get_user_model()


# Create Profile Automatically when a new user register
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profiles.objects.create(user=instance, first_name=instance.first_name,
                                last_name=instance.last_name, email=instance.email)

post_save.connect(create_profile, sender=User)