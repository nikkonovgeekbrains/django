from django.contrib import admin

# Register your models here.
from django.contrib import admin

from authapp.models import ShopUser

admin.site.register(ShopUser)
