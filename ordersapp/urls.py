from django.urls import path
import ordersapp.views as ordersapp
from django.urls import re_path

app_name = 'ordersapp'

urlpatterns = [
    path('', ordersapp.OrderListView.as_view(), name='orders_list'),
    path('create/', ordersapp.OrderItemsCreateView.as_view(), name='order_create'),
    path('read/<int:pk>/', ordersapp.OrderReadView.as_view(), name='order_read'),
    path('update/<int:pk>/', ordersapp.OrderItemsUpdateView.as_view(), name='order_update'),
    path('delete/<int:pk>/', ordersapp.OrderDeleteView.as_view(), name='order_delete'),

    path('forming/complete/<int:pk>/', ordersapp.order_forming_complete, name='order_forming_complete'),
]
