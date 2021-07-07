from django.shortcuts import HttpResponseRedirect
from products.models import Product
from baskets.models import Basket

def basket_add(request, product_id):

    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if baskets.exists():
        basket = baskets.last()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    Basket.objects.create(user=request.user, product=product, quantity=1)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))