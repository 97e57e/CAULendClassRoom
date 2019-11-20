from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=10)
    user_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=13)
    birth = models.DateField(default=datetime.date.today)
    userType = models.CharField(max_length=10)
    department = models.CharField(max_length=20)

    def __str__(self):
        return self.user_code

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()