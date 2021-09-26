from django.core.management import BaseCommand
from django.db.models import Q, F, When, Case, DecimalField, Sum, ExpressionWrapper

from orders.models import OrderItem


class Command(BaseCommand):

    # Я решила не копипастить то, что было на уроке, а попробовать написать свой запрос.
    # Здесь выводятся заказы и стоимость доставки, из расчёта, что бесплатная доставка начинается от
    # суммы заказа 4000 рублей, а в прочих случаях составляет 5% от стоимости заказа.
    # Получилось не так объёмно, как той задаче, что на уроке, но зато разобралась
    # как реализуется группировка и агрегационные методы.

    def handle(self, *args, **options):
        action_1__delivery = 0.05
        action_2__delivery = 0

        action_1__condition = Q(order_price__gte=4000)
        action_2__condition = Q(order_price__lt=4000)

        action_1__price = When(action_1__condition,
                               then=ExpressionWrapper(F('order_price') * action_2__delivery,
                                                      output_field=DecimalField()))
        action_2__price = When(action_2__condition,
                               then=ExpressionWrapper(F('order_price') * action_1__delivery,
                                                      output_field=DecimalField()))

        base_orders = OrderItem.objects.values('order_id').annotate(
            order_price=Sum(F('product__price') * F('quantity'), output_field=DecimalField()),
            delivery_price=Case(
                action_1__price,
                action_2__price,
                output_field=DecimalField()
            )
        ).order_by('delivery_price', 'order_id')

        for order in base_orders:
            print(f'№ заказа:{order.get("order_id"):3} \t\t'
                  f'Сумма заказа: {order.get("order_price"):9.2f} руб.\t\t'
                  f'Доставка: {order.get("delivery_price"):5.2f} руб.')
