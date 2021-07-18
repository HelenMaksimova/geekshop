from django.urls import path
from admins.views import (
    index,
    AdminUserListView, AdminUserCreateView, AdminUserUpdateView, AdminUserDeleteView,
    AdminCategoryListView, AdminCategoryCreateView, AdminCategoryUpdateView, AdminCategoryDeleteView,
    AdminGoodListView, AdminGoodCreateView, AdminGoodUpdateView, AdminGoodDeleteView,
)

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/read/', AdminUserListView.as_view(), name='users_read'),
    path('users/create/', AdminUserCreateView.as_view(), name='users_create'),
    path('users/update/<int:pk>/', AdminUserUpdateView.as_view(), name='users_update'),
    path('users/delete/<int:pk>/', AdminUserDeleteView.as_view(), name='users_delete'),
    path('categories/read/', AdminCategoryListView.as_view(), name='categories_read'),
    path('categories/create/', AdminCategoryCreateView.as_view(), name='categories_create'),
    path('categories/update/<int:pk>/', AdminCategoryUpdateView.as_view(), name='categories_update'),
    path('categories/delete/<int:pk>/', AdminCategoryDeleteView.as_view(), name='categories_delete'),
    path('goods/read/', AdminGoodListView.as_view(), name='goods_read'),
    path('goods/create/', AdminGoodCreateView.as_view(), name='goods_create'),
    path('goods/update/<int:pk>/', AdminGoodUpdateView.as_view(), name='goods_update'),
    path('goods/delete/<int:pk>/', AdminGoodDeleteView.as_view(), name='goods_delete'),
]
