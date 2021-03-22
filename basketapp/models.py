from django.db import models

# Create your models here.

from django.db import models
from django.conf import settings
from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    @property
    def sum_quant(self):
        basket_list = Basket.objects.filter(user=self.user)
        sum_q = 0
        for el in basket_list:
            sum_q += el.quantity
        return sum_q

    @property
    def sum_coast(self):
        basket_list = Basket.objects.filter(user=self.user)
        sum_c = 0
        for el in basket_list:
            sum_c += el.quantity * el.product.price
        return sum_c
