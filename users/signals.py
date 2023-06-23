import datetime

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.signals import user_login_failed


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(user_login_failed)
def save_failed_attempt(sender, credentials, request, **kwargs):
    username = credentials.get("username")
    user = User.objects.filter(username=username)
    if user:
        profile = Profile.objects.filter(user_id=user[0].id)[0]
        profile.last_failed_attempt = datetime.datetime.now()
        profile.save()

