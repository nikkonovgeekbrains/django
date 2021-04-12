from django import template
from django.conf import settings

register = template.Library()

@register.filter(name='media_for_users')
def media_for_users(path_to_avatar):
    """
    Автоматически добавляет относительный URL-путь к медиафайлам пользователей
    users_avatars/user1.jpg --> /media/users_avatars/user1.jpg
    """
    if not path_to_avatar:
        path_to_avatar = 'users_avatars/default.jpg'

    return f'{settings.MEDIA_URL}{path_to_avatar}'

def media_for_products(path_to_prod_img):
    """
    Автоматически добавляет относительный URL-путь к медиафайлам пользователей
    users_avatars/user1.jpg --> /media/users_avatars/user1.jpg
    """
    if not path_to_prod_img:
        path_to_prod_img = 'products_images/default.jpg'

    return f'{settings.MEDIA_URL}{path_to_prod_img}'


register.filter('media_for_products', media_for_products)
