from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta

class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name = 'возраст')

    activation_key = models.CharField(max_length=128, blank=True)
#    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))
    activation_key_expires = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def is_activation_key_expired(self):
        now_date = now() - timedelta(hours=48)
        if now_date <= self.activation_key_expires:
            return False
        else:
            return True
