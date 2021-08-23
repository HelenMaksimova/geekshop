from products.models import Product, ProductCategory
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.conf import settings
from django.core.cache import cache


def get_categories_all():
    if settings.LOW_CACHE:
        key = 'categories_all'
        categories_all = cache.get(key)
        if categories_all is None:
            categories_all = ProductCategory.objects.all()
            cache.set(key, categories_all)
        return categories_all
    else:
        return ProductCategory.objects.all()


def get_products_all():
    if settings.LOW_CACHE:
        key = 'products_all'
        products_all = cache.get(key)
        if products_all is None:
            products_all = Product.objects.all().select_related('category').order_by('pk')
            cache.set(key, products_all)
        return products_all
    else:
        return Product.objects.all().select_related('category').order_by('pk')


def get_products_in_category(pk):
    if settings.LOW_CACHE:
        key = f'products_in_category_{pk}'
        products_in_category = cache.get(key)
        if products_in_category is None:
            products_in_category = Product.objects.filter(category__pk=pk).order_by('pk')
            cache.set(key, products_in_category)
        return products_in_category
    else:
        return Product.objects.filter(category__pk=pk).order_by('pk')


class IndexTemplateView(TemplateView):
    extra_context = {'title': 'GeekShop'}
    template_name = 'products/index.html'


class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3
    extra_context = {
        'title': 'GeekShop - Каталог',
        'categories': get_categories_all()
    }

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return get_products_in_category(category_id) if category_id else get_products_all()


