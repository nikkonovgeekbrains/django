from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlencode, urlunparse

import requests
from django.utils import timezone
from social_core.exceptions import AuthForbidden

from authapp.models import ShopUserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return

    api_url = urlunparse(('https',
                          'api.vk.com',
                          '/method/users.get',
                          None,
                          urlencode(OrderedDict(fields=','.join(('bdate', 'sex', 'about', 'city', 'photo_max')), access_token=response['access_token'], v='5.92')),
                          None
                          ))

    resp = requests.get(api_url)
    if resp.status_code != 200:
        return
    print(resp.json())
    data = resp.json()['response'][0]

    if data['sex']:
        if data['sex'] == 1:
            user.shopuserprofile.gender = ShopUserProfile.FEMALE
        elif data['sex'] == 2:
            user.shopuserprofile.gender = ShopUserProfile.MALE

    if data['about']:
        user.shopuserprofile.aboutMe = data['about']

    if data['photo_max']:
        user_vk_avatar = requests.get(data['photo_max'])
        if user_vk_avatar.status_code == 200:
            with open(f'media/users_avatars/user_{user.username}.jpg', 'wb') as img:
                img.write(user_vk_avatar.content)
                user.avatar = f'users_avatars/user_{user.username}.jpg'

    if data['bdate']:
        bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()
        # age = timezone.now().date().year - bdate.year
        age = datetime.now().date().year - bdate.year
        user.age = age

        if age < 18:
            user.delete()
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')

    user.save()
