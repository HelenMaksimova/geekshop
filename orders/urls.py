from django.urls import path

from orders.views import OrderListView, OrderCreateView, OrderDeleteView, OrderUpdateView, OrderDetailView

app_name = 'orders'

urlpatterns = [
    path('', OrderListView.as_view(), name='list'),
    path('read/<int:pk>/', OrderDetailView.as_view(), name='read'),
    path('update/<int:pk>/', OrderUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', OrderDeleteView.as_view(), name='delete'),
    path('create/', OrderCreateView.as_view(), name='create'),

]
