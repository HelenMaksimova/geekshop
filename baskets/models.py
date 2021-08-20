from django.db import models
from users.models import User
from products.models import Product


class Basket(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Товар {self.product.name}'

    @property
    def elements(self):
        return Basket.objects.filter(user=self.user).select_related()

    @property
    def total_quantity(self):
        return sum(list(item.quantity for item in self.elements))

    @property
    def total_sum(self):
        return sum(list(item.sum() for item in self.elements))

    def sum(self):
        return self.quantity * self.product.price
