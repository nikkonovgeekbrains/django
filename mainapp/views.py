from django.shortcuts import render
import datetime
import os
from django.conf import settings
import json

from mainapp.models import ProductCategory, Product

from django.shortcuts import get_object_or_404
from basketapp.models import Basket

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
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    #basket = 0
    #if request.user.is_authenticated:
        #basket = sum(list(Basket.objects.filter(user=request.user).values_list('quantity', flat=True)))
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
            'basket': basket
        }
        return render(request, 'mainapp/products_list.html', content)

    same_products = Product.objects.all()[:4]
    content = {
        'title': tittel,
        'links_menu': links_menu,
        'same_products': same_products,
        'basket': basket
    }
    print(basket)
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
