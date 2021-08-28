from django.test import TestCase
from products.models import ProductCategory, Product
from baskets.models import Basket
from django.test.client import Client
from users.models import User

STATUS_CODE_ACCESS = 200
STATUS_CODE_REDIRECT = 301
STATUS_CODE_LOGIN_REDIRECT = 302
USERNAME = 'django'
PASSWORD = 'geekbrains'
EMAIL = 'geek@shop.com'


class BasketModelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(USERNAME, EMAIL, PASSWORD)
        self.category = ProductCategory.objects.create(name='категория')
        self.product1 = Product.objects.create(name='товар1', price=100, quantity=10, category=self.category)
        self.product2 = Product.objects.create(name='товар2', price=200, quantity=10, category=self.category)
        self.product3 = Product.objects.create(name='товар3', price=300, quantity=10, category=self.category)
        self.basket1 = Basket.objects.create(user=self.user, product=self.product1, quantity=1)
        self.basket2 = Basket.objects.create(user=self.user, product=self.product2, quantity=2)
        self.basket3 = Basket.objects.create(user=self.user, product=self.product3, quantity=3)

    def test_basket_str(self):
        self.assertEqual(str(self.basket1), f'Корзина для {self.user.username} | Товар {self.product1.name}')

    def test_elements(self):
        self.assertEqual(
            list(self.basket2.elements),
            [self.basket1, self.basket2, self.basket3]
        )

    def test_product_price(self):
        self.assertEqual(
            [basket.product_price for basket in self.basket3.elements],
            [100, 200, 300]
        )

    def test_get_summary(self):
        self.assertEqual(
            self.basket1.get_summary(),
            {'total_quantity': 6, 'total_sum': 1400}
        )

    def test_total_quantity(self):
        self.assertEqual(self.basket1.total_quantity(), 6)

    def test_total_sum(self):
        self.assertEqual(self.basket1.total_sum(), 1400)

    def test_sum(self):
        self.assertEqual(
            [basket.sum() for basket in self.basket3.elements],
            [100, 400, 900]
        )
