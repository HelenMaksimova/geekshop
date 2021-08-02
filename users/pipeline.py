from datetime import datetime
from django.utils import timezone
import requests
from social_core.exceptions import AuthForbidden
from users.models import UserProfile


def save_user_profile(backend, user, response, *args, **kwargs):

    if backend.name != 'vk-oauth2':
        return

    api_url = 'https://api.vk.com/method/users.get'
    fields_tuple = ('bdate', 'sex', 'about', 'has_photo', 'photo_max_orig')
    params = {
        'fields': ','.join(fields_tuple),
        'access_token': response['access_token'],
        'v': '5.92',
    }

    api_response = requests.get(api_url, params=params)

    if api_response.status_code != 200:
        return

    data = api_response.json()['response'][0]
    if data.get('sex'):
        user.userprofile.gender = UserProfile.MALE if data['sex'] == 2 else UserProfile.FEMALE

    if data.get('about'):
        user.userprofile.aboutMe = data['about']

    if data.get('bdate'):
        bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()
        user.birthday = bdate

        age = timezone.now().date().year - bdate.year
        if age < 18:
            user.delete()
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')
        user.userprofile.age = age

    if data.get('has_photo'):
        photo_url = data.get('photo_max_orig')
        result = requests.get(photo_url, stream=True)
        result.raw.decode_content = True
        user.image.save(f'avatar{user.id}.jpg', result.raw)

    user.save()
