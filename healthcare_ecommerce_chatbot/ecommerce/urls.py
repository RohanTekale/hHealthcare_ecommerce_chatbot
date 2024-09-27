from django.urls import path
from .views import ProductListView, OrderCreateView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),  # List and create products
    path('orders/', OrderCreateView.as_view(), name='order-create'),     # Create orders
]
