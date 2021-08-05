from products.models import Product, ProductCategory
from django.views.generic.list import ListView
from django.views.generic import TemplateView


class IndexTemplateView(TemplateView):
    extra_context = {'title': 'GeekShop'}
    template_name = 'products/index.html'


class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3
    extra_context = {
        'title': 'GeekShop - Каталог',
        'categories': ProductCategory.objects.all(),
    }

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
