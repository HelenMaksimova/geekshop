from django.shortcuts import render
from products.models import Product, ProductCategory


def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    products_list = Product.objects.all() if not category_id else Product.objects.filter(category_id=category_id)
    context = {
        'title': 'GeekShop - Каталог',
        'products': products_list,
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products/products.html', context)
