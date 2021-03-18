from django.shortcuts import render
import datetime
import os
from django.conf import settings
import json

from mainapp.models import ProductCategory, Product

# Create your views here.
def main(request):
    title = 'Главная'
    # products = [
    #     {
    #         'name': 'Отличный стул',
    #         'desc': 'Расположитесь комфортно',
    #         'image_src': 'product-1.jpg',
    #         'image_href': '/product/1/',
    #         'alt': 'продукт 1',
    #     },
    #     {
    #         'name': 'Стул повышенного качества',
    #         'desc': 'Не оторваться',
    #         'image_src': 'product-2.jpg',
    #         'image_href': '/product/2/',
    #         'alt': 'продукт 2',
    #     },
    # ]

    products = Product.objects.all()[:4]

    content = {
        'title': title,
        'products': products,
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    tittel = 'Продукты'
    # links_menu = [
    #     {'href': 'products_all', 'name': 'все'},
    #     {'href': 'products_home', 'name': 'дом'},
    #     {'href': 'products_office', 'name': 'офис'},
    #     {'href': 'products_modern', 'name': 'модерн'},
    #     {'href': 'products_classic', 'name': 'классика'}
    # ]

    links_menu = ProductCategory.objects.all()
    same_products = Product.objects.all()[:4]
    content = {
        'title': tittel,
        'links_menu': links_menu,
        'same_products': same_products,
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    title = 'Контакты'
    locations = []
    with open(os.path.join(settings.BASE_DIR ,'contacts.json'), encoding="utf-8") as f:
        locations = json.load(f)
    content = {
        'title': title,
        'locations': locations,
    }
    return render(request, 'mainapp/contact.html', content)
