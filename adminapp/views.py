from django.contrib.auth.decorators import user_passes_test

from django.shortcuts import render

# Create your views here.
from adminapp.forms import ShopUserAdminEditForm, ProductCategoryEditForm, ProductEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from django.shortcuts import get_object_or_404, render
from mainapp.models import Product, ProductCategory
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:user_read'))
    else:
        user_form = ShopUserRegisterForm()

    content = {'title': 'пользователи/создание',
               'form': user_form}

    return render(request, 'adminapp/user_update.html', content)

@user_passes_test(lambda u: u.is_superuser)
def users(request):
    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    content = {
        'title': 'админка/пользователи',
        'objects': users_list
    }

    return render(request, 'adminapp/users.html', content)

@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        user_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:user_read'))
    else:
        user_form = ShopUserAdminEditForm(instance=edit_user)

    content = {'title': 'пользователи/редактирование',
               'form': user_form}

    return render(request, 'adminapp/user_update.html', content)

@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        if user.is_active:
            user.is_active = False
        else:
            user.is_active = True
        user.save()
        return HttpResponseRedirect(reverse('admin:user_read'))

    content = {'title': 'пользователи/удаление',
               'user_to_delete': user}

    return render(request, 'adminapp/user_delete.html', content)

@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    if request.method == 'POST':
        category_form = ProductCategoryEditForm(request.POST, request.FILES)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('admin:category_read'))
    else:
        category_form = ProductCategoryEditForm()

    content = {'title': 'категории/создание',
               'form': category_form}

    return render(request, 'adminapp/category_update.html', content)

@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    categories_list = ProductCategory.objects.all()

    content = {
        'title': 'админка/категории',
        'objects': categories_list
    }

    return render(request, 'adminapp/categories.html', content)

@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk):
    edit_category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        category_form = ProductCategoryEditForm(request.POST, request.FILES, instance=edit_category)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('admin:category_read'))
    else:
        category_form = ProductCategoryEditForm(instance=edit_category)

    content = {'title': 'категории/редактирование',
               'form': category_form}

    return render(request, 'adminapp/category_update.html', content)

@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        if category.is_active:
            category.is_active = False
        else:
            category.is_active = True
        category.save()
        return HttpResponseRedirect(reverse('admin:category_read'))

    content = {'title': 'категории/удаление',
               'category_to_delete': category}

    return render(request, 'adminapp/category_delete.html', content)

@user_passes_test(lambda u: u.is_superuser)
def product_create(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin:products', args=[pk]))
    else:
        product_form = ProductEditForm(initial={'category': category})

    content = {'title': 'продукты/создание',
               'form': product_form,
               'category': category
               }

    return render(request, 'adminapp/category_update.html', content)

@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    category_item = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    content = {
        'title': 'админка/продукт',
        'category': category_item,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', content)

@user_passes_test(lambda u: u.is_superuser)
def product_read(request, pk):
    product = get_object_or_404(Product, pk=pk)
    content = {'title': 'продукт/подробнее', 'object': product, }

    return render(request, 'adminapp/product_detail.html', content)

@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    edit_product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        update_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
        if update_form.is_valid():
            update_form.save()
            return HttpResponseRedirect(reverse('admin:products', args=[edit_product.category_id]))
    else:
        update_form = ProductEditForm(instance=edit_product)

    content = {'title': 'продукты/редактирование',
               'form': update_form,
               'category': edit_product.category,
               }

    return render(request, 'adminapp/product_update.html', content)

@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        if product.is_active:
            product.is_active = False
        else:
            product.is_active = True
        product.save()
        return HttpResponseRedirect(reverse('admin:products', args=[product.category.pk]))

    content = {'title': 'продукты/удаление',
               'product_to_delete': product,
               }

    return render(request, 'adminapp/product_delete.html', content)
