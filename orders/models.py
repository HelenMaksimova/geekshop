from django.db import models
from django.conf import settings
from products.models import Product
from django.utils.functional import cached_property


class Order(models.Model):
    FORMING = 'FM'
    SENT_TO_PROCEED = 'STP'
    DELIVERY = 'DLV'
    DONE = 'DN'
    CANCELED = 'CNC'

    ORDER_STATUS_CHOICES = (
        (FORMING, 'формирование'),
        (SENT_TO_PROCEED, 'отправлен в обработку'),
        (DELIVERY, 'доставляется'),
        (DONE, 'выполнен'),
        (CANCELED, 'отменен'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=ORDER_STATUS_CHOICES, default=FORMING)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return f'Заказ {self.id}'

    @cached_property
    def elements(self):
        return self.orderitems.select_related()

    def get_summary(self):
        items = self.elements
        return {
            'total_quantity': sum(map(lambda x: x.quantity, items)),
            'total_cost': sum(map(lambda x: x.get_product_cost, items)),
        }

    def get_total_quantity(self):
        items = self.elements
        return sum(map(lambda x: x.quantity, items))

    def get_total_cost(self):
        items = self.elements
        return sum(map(lambda x: x.get_product_cost, items))

    def delete(self):
        self.is_active = False
        self.save()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="orderitems", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    @cached_property
    def product_price(self):
        return self.product.price

    @property
    def get_product_cost(self):
        return self.product_price * self.quantity

