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

    @classmethod
    def total_quantity(cls, user):
        elements = cls.objects.filter(user=user)
        return sum(item.quantity for item in elements)

    @classmethod
    def total_sum(cls, user):
        elements = cls.objects.filter(user=user)
        return sum(item.sum() for item in elements)

    def sum(self):
        return self.quantity * self.product.price
