from django.contrib import admin
from django.urls import path
from mainapp import views as mainapp
from django.conf.urls import include
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='products'),
    path('<int:pk>/', mainapp.products, name='category'),
    path('product/<int:pk>/', mainapp.product, name='product')
]

# urlpatterns = [
#     re_path(r'^$', mainapp.products, name='products'),
#     re_path(r'^category/(?P<pk>\d+)/$', mainapp.products, name='category'),
#     re_path(r'^product/(?P<pk>\d+)/$', mainapp.product, name='product'),
#     #re_path(r'^category/(?P<pk>\d+)/page/(?P<page>\d+)/$', mainapp.products, name='page'),
# ]

