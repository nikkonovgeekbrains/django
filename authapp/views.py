from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import ShopUserLoginForm
from django.contrib import auth
from django.urls import reverse
from authapp.forms import ShopUserRegisterForm
from authapp.forms import ShopUserEditForm

from django.core.mail import send_mail
from django.conf import settings
from authapp.models import ShopUser


def login(request):
    title = 'вход'

    login_form = ShopUserLoginForm(data=request.POST)

    #next = request.GET.get('next', '')
    next = request.GET['next'] if 'next' in request.GET else ''

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST:
                return HttpResponseRedirect(request.POST['next'])
            return HttpResponseRedirect(reverse('main'))

    content = {'title': title,
               'login_form': login_form,
               'next': next}
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


def register(request):
    title = 'регистрация'

    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            user = register_form.save()
            if send_verify_email(user):
                print('success')
            else:
                print('failed')
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()

    content = {'title': title, 'register_form': register_form}

    return render(request, 'authapp/register.html', content)


def edit(request):
    title = 'редактирование'

    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)

    content = {'title': title, 'edit_form': edit_form}

    return render(request, 'authapp/edit.html', content)


def send_verify_email(user):
    verify_link = reverse('authapp:verify', args=[user.email, user.activation_key])

    subject = f'Подтверждение учетной записи {user.email}'

    message = f'Ссылка для активации: {settings.DOMAIN_NAME}{verify_link}'

    return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

def verify(request, email, activation_key):
    user = ShopUser.objects.get(email=email)
    if user.activation_key == activation_key and not user.is_activation_key_expired():
        user.is_active = True
        user.activation_key = ''
        user.save()
        auth.login(request, user)
    return render(request, 'authapp/verification.html')

