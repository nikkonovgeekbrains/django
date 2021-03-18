from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product

import json, os

from authapp.models import ShopUser


JSON_PATH = 'mainapp/json'

def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r',  encoding="utf-8") as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')
        ProductCategory.objects.all().delete()
        for cat in categories:
            new_category = ProductCategory(**cat)
            new_category.save()

        products = load_from_json('products')
        Product.objects.all().delete()

        for prod in products:
            category_name = prod["category"]
            _cat = ProductCategory.objects.get(name=category_name)
            prod['category'] = _cat
            new_product = Product(**prod)
            new_product.save()

        super_user = ShopUser.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains', age = 18)