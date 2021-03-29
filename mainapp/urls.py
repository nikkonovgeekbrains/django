from django.contrib import admin
from django.urls import path
from mainapp import views as mainapp
from django.conf import settings
from django.conf.urls.static import static

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='products'),
    path('<int:pk>/', mainapp.products, name='category'),
    path('product/<int:pk>/', mainapp.product, name='product')
]

