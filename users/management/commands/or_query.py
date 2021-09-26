from django.core.management import BaseCommand
from django.db.models import Q, Count

from products.models import Product
from orders.models import Order, OrderItem


class Command(BaseCommand):

    def handle(self, *args, **options):
        result = Product.objects.filter(
            Q(price__gte=2000) | Q(category__name='Аксесуары')
        )
        print(result)

        condition_1 = Q(product__category__name='Аксесуары')
        condition_2 = Q(product__category__name='Обувь')
        result = OrderItem.objects.filter(condition_1 | condition_2)\
            .values('order_id')\
            .annotate(items_count=Count('order_id'))
        print(result)
