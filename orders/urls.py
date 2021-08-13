from django.urls import path

from orders.views import OrderListView, OrderCreateView, OrderDeleteView, \
    OrderUpdateView, OrderDetailView, order_forming_complete, order_item_price

app_name = 'orders'

urlpatterns = [
    path('', OrderListView.as_view(), name='list'),
    path('read/<int:pk>/', OrderDetailView.as_view(), name='read'),
    path('update/<int:pk>/', OrderUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', OrderDeleteView.as_view(), name='delete'),
    path('create/', OrderCreateView.as_view(), name='create'),
    path('forming/complete/<int:pk>/', order_forming_complete, name='order_forming_complete'),
    path('order_item_price/<int:pk>/', order_item_price, name='order_item_price'),
]
