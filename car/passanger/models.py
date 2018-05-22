from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class PassengerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    profile_pic = models.ImageField(
        upload_to='profile/passenger/', default='/media/profile/passenger/user.svg', null=True)
    age = models.IntegerField(null=True)

    def getPic(self):
        if not self.profile_pic:
            return '/media/profile/driver/user.svg'
