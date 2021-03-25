from django.shortcuts import render
import datetime
import os
from django.conf import settings
import json

from mainapp.models import ProductCategory, Product

from django.shortcuts import get_object_or_404
from basketapp.models import Basket

import random

# Create your views here.

def get_basket(user):
    basket = []
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    return []


def get_hot_product():
    products_list = Product.objects.all()

    return random.sample(list(products_list), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return same_products

def main(request):
    title = 'Главная'
    products = Product.objects.all()[:4]

    content = {
        'title': title,
        'products': products,
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    print(pk)
    tittel = 'Продукты'
    links_menu = ProductCategory.objects.all()
    if pk is not None:
        if pk == 0:
            product_list = Product.objects.all().order_by('price')
            category_item = {'name': 'все', 'pk': 0}
        else:
            category_item = get_object_or_404(ProductCategory, pk=pk)
            product_list = Product.objects.filter(category=category_item)
        content = {
            'title': tittel,
            'links_menu': links_menu,
            'category': category_item,
            'products': product_list,
            'basket': get_basket(request.user),
        }
        return render(request, 'mainapp/products_list.html', content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    content = {
        'title': tittel,
        'links_menu': links_menu,
        'same_products': same_products,
        'hot_product': hot_product,
        'basket': get_basket(request.user),
    }
    #print(basket)
    return render(request, 'mainapp/products.html', content)


def contact(request):
    title = 'Контакты'
    locations = []
    with open(os.path.join(settings.BASE_DIR ,'contacts.json'), encoding="utf-8") as f:
        locations = json.load(f)
    content = {
        'title': title,
        'locations': locations,
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/contact.html', content)


def product(request, pk):
    content = {
        'title': 'продукты',
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/product.html', content)