from django.shortcuts import HttpResponseRedirect
from products.models import Product
from baskets.models import Basket
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import F


@login_required
def basket_add(request, product_id):

    product = Product.objects.filter(id=product_id).select_related().first()
    baskets = Basket.objects.filter(user=request.user, product=product).select_related()

    if baskets.exists():
        basket = baskets.last()
        basket.quantity = F('quantity') + 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    Basket.objects.create(user=request.user, product=product, quantity=1)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, id):
    basket = Basket.objects.filter(id=id).select_related().first()
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, id, quantity):
    if request.is_ajax():
        basket = Basket.objects.filter(id=id).select_related().first()
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()
    context = {
        'baskets': Basket.objects.filter(user=request.user).select_related(),
    }
    result = render_to_string('baskets/basket.html', context)
    return JsonResponse({'result': result})
