from django.test import TestCase
from django.test.client import Client
from products.models import ProductCategory
from django.core.management import call_command

STATUS_CODE_ACCESS = 200
STATUS_CODE_REDIRECT = 301


class ProductsSmokeTest(TestCase):

    def setUp(self):
        call_command('loaddata', 'categories.json')
        call_command('loaddata', 'products.json')
        self.client = Client()

    def test_products_urls(self):

        response = self.client.get('/')
        self.assertEqual(response.status_code, STATUS_CODE_ACCESS)

        response = self.client.get('/products/')
        self.assertEqual(response.status_code, STATUS_CODE_ACCESS)

        for category in ProductCategory.objects.all():
            response = self.client.get(f'/products/{category.pk}')
            self.assertEqual(response.status_code, STATUS_CODE_REDIRECT)
