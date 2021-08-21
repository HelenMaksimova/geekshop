from django.db import models
from users.models import User
from products.models import Product
from django.utils.functional import cached_property


class Basket(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Товар {self.product.name}'

    @cached_property
    def elements(self):
        return Basket.objects.filter(user=self.user).select_related()

    @cached_property
    def product_price(self):
        return self.product.price

    def total_quantity(self):
        return sum(list(item.quantity for item in self.elements))

    def total_sum(self):
        return sum(list(item.sum() for item in self.elements))

    def sum(self):
        return self.quantity * self.product_price
