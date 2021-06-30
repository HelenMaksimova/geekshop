# Это файл с тем кодом, который я вводила к консоли для первоначального заполнения базы из json.
# Он справочный, подгружен в проект для наглядности, самих json_файлов уже нет, они заменены дампами базы.

# from products.models import Product, ProductCategory
# from json import load
#
# data_category = load(open('products/fixtures/categories.json', encoding='utf-8'))
# data_products = load(open('products/fixtures/products.json', encoding='utf-8'))
#
# category_objects = [ProductCategory(**item) for item in data_category]
#
# ProductCategory.objects.bulk_create(category_objects)
#
# category_objects = ProductCategory.objects.all()
#
# for product in data_products:
#     product['category'] = category_objects[product['category'] - 1]
#
# product_objects = [Product(**item) for item in data_products]
#
# Product.objects.bulk_create(product_objects)
