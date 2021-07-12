from django import template
from baskets.models import Basket


def total_sum(*args, **kwargs):
    return Basket.total_sum(*args, **kwargs)


def total_quantity(*args, **kwargs):
    return Basket.total_quantity(*args, **kwargs)


register = template.Library()

register.simple_tag(total_sum, name='total_sum')
register.simple_tag(total_quantity, name='total_quantity')