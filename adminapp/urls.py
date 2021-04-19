import adminapp.views as adminapp
from django.urls import path
from django.urls import re_path

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', adminapp.user_create, name='user_create'),
    #path('users/read/', adminapp.users, name='user_read'),
    path('users/read/', adminapp.UsersListView.as_view(), name='user_read'),
    path('users/update/<int:pk>/', adminapp.user_update, name='user_update'),
    path('users/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),

    #path('categories/create', adminapp.category_create, name='category_create'),
    path('categories/create', adminapp.ProductCategoryCreateView.as_view(), name='category_create'),
    path('categories/read/', adminapp.categories, name='category_read'),
    #path('categories/update/<int:pk>/', adminapp.category_update, name='category_update'),
    path('categories/update/<int:pk>/', adminapp.ProductCategoryUpdateView.as_view(), name='category_update'),
    #path('categories/delete/<int:pk>/', adminapp.category_delete, name='category_delete'),
    path('categories/delete/<int:pk>/', adminapp.ProductCategoryDeleteView.as_view(), name='category_delete'),
    #path('products/create/category/<int:pk>/', adminapp.product_create, name='product_create'),
    path('products/create/category/<int:pk>/', adminapp.ProductCreateView.as_view(), name='product_create'),
    #path('products/read/category/<int:pk>/', adminapp.products, name='products'),
    path('products/read/category/<int:pk>/', adminapp.ProductListView.as_view(), name='products'),
    #path('products/read/<int:pk>/', adminapp.product_read, name='product_read'),
    path('products/read/<int:pk>/', adminapp.ProductDetailView.as_view(), name='product_read'),
    #path('products/update/<int:pk>/', adminapp.product_update, name='product_update'),
    path('products/update/<int:pk>/', adminapp.ProductUpdateView.as_view(), name='product_update'),
    #path('products/delete/<int:pk>/', adminapp.product_delete, name='product_delete'),
    path('products/delete/<int:pk>/', adminapp.ProductDeleteView.as_view(), name='product_delete'),
]

# urlpatterns = [
#     re_path(r'users/create/', adminapp.user_create, name='user_create'),
#     re_path(r'users/read/', adminapp.UsersListView.as_view(), name='user_read'),
#     re_path(r'users/update/(?P<pk>\d+)/', adminapp.user_update, name='user_update'),
#     re_path(r'users/delete/(?P<pk>\d+)/', adminapp.user_delete, name='user_delete'),
#     re_path(r'categories/create', adminapp.ProductCategoryCreateView.as_view(), name='category_create'),
#     re_path(r'categories/read/', adminapp.categories, name='category_read'),
#     re_path(r'categories/update/(?P<pk>\d+)/', adminapp.ProductCategoryUpdateView.as_view(), name='category_update'),
#     re_path(r'categories/delete/(?P<pk>\d+)/', adminapp.ProductCategoryDeleteView.as_view(), name='category_delete'),
#     re_path(r'products/create/category/(?P<pk>\d+)/', adminapp.ProductCreateView.as_view(), name='product_create'),
#     re_path(r'products/read/category/(?P<pk>\d+)/', adminapp.ProductListView.as_view(), name='products'),
#     re_path(r'products/read/(?P<pk>\d+)/', adminapp.ProductDetailView.as_view(), name='product_read'),
#     re_path(r'products/update/(?P<pk>\d+)/', adminapp.ProductUpdateView.as_view(), name='product_update'),
#     re_path(r'products/delete/(?P<pk>\d+)/', adminapp.ProductDeleteView.as_view(), name='product_delete'),
# ]
