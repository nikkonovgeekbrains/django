from django.urls import path

import basketapp.views as basketapp
from django.conf.urls import include
from django.urls import re_path

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.basket, name='view'),
    path('add/<int:pk>/', basketapp.basket_add, name='add'),
    path('remove/<int:pk>)/', basketapp.basket_remove, name='remove'),
    path('edit/<int:pk>/<int:quantity>/', basketapp.basket_edit, name='edit'),
]

# urlpatterns = [
#     re_path(r'^$', basketapp.basket, name='view'),
#     re_path(r'^add/(?P<pk>\d+)/$', basketapp.basket_add, name='add'),
#     re_path(r'^remove/(?P<pk>\d+)/$', basketapp.basket_remove, name='remove'),
#     re_path(r'^edit/(?P<pk>\d+)/(?P<quantity>\d+)/$', basketapp.basket_edit, name='edit'),
# ]
