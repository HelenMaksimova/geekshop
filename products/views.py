from django.shortcuts import render
from products.models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page=1):
    products_list = Product.objects.all() if not category_id else Product.objects.filter(category_id=category_id)
    paginator = Paginator(products_list, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context = {
        'title': 'GeekShop - Каталог',
        'products': products_paginator,
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products/products.html', context)
