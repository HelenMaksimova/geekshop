from django.urls import path
from admins.views import (
    index,
    admin_users_read, admin_users_create,
    admin_users_update, admin_users_delete,
    admin_categories_read, admin_categories_create,
    admin_categories_update, admin_categories_delete,
    admin_goods_read, admin_goods_create,
    admin_goods_update, admin_goods_delete,
)

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/read/', admin_users_read, name='users_read'),
    path('users/create/', admin_users_create, name='users_create'),
    path('users/update/<int:id>/', admin_users_update, name='users_update'),
    path('users/delete/<int:id>/', admin_users_delete, name='users_delete'),
    path('categories/read/', admin_categories_read, name='categories_read'),
    path('categories/create/', admin_categories_create, name='categories_create'),
    path('categories/update/<int:id>/', admin_categories_update, name='categories_update'),
    path('categories/delete/<int:id>/', admin_categories_delete, name='categories_delete'),
    path('goods/read/', admin_goods_read, name='goods_read'),
    path('goods/create/', admin_goods_create, name='goods_create'),
    path('goods/update/<int:id>/', admin_goods_update, name='goods_update'),
    path('goods/delete/<int:id>/', admin_goods_delete, name='goods_delete'),
]
