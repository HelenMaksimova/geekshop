from django.test import TestCase
from django.test.client import Client
from users.models import User

STATUS_CODE_ACCESS = 200
STATUS_CODE_REDIRECT = 301
STATUS_CODE_LOGIN_REDIRECT = 302
USERNAME = 'django'
PASSWORD = 'geekbrains'
EMAIL = 'geek@shop.com'


class UsersTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(USERNAME, EMAIL, PASSWORD)
        self.client = Client()

    def test_user_login(self):

        # без логина на главную
        response = self.client.get('/')
        self.assertEqual(response.status_code, STATUS_CODE_ACCESS)
        self.assertTrue(response.context['user'].is_anonymous)
        self.assertNotContains(response, 'Выйти', status_code=STATUS_CODE_ACCESS)

        # логин
        self.client.login(username=USERNAME, password=PASSWORD)
        response = self.client.get('/users/login/')
        self.assertFalse(response.context['user'].is_anonymous)
        self.assertEqual(response.context['user'], self.user)

        # с логином на главную
        response = self.client.get('/')
        self.assertContains(response, self.user.username, status_code=STATUS_CODE_ACCESS)
        self.assertEqual(response.context['user'], self.user)

    def test_basket_login_redirect(self):

        # без логина
        response = self.client.get(f'/users/profile/{self.user.pk}/')
        self.assertEqual(response.url, f'/users/login/?next=/users/profile/{self.user.pk}/')
        self.assertEqual(response.status_code, STATUS_CODE_LOGIN_REDIRECT)

        # с логином
        self.client.login(username=USERNAME, password=PASSWORD)
        response = self.client.get(f'/users/profile/{self.user.pk}/')
        self.assertEqual(response.status_code, STATUS_CODE_ACCESS)
        self.assertEqual(list(response.context['baskets']), [])
        self.assertEqual(response.request['PATH_INFO'], f'/users/profile/{self.user.pk}/')
        self.assertContains(response, 'Корзина пуста')
