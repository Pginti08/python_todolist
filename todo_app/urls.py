from django.urls import path
from .views import create_product, list_products, update_product, delete_product

urlpatterns = [
    path('create/', create_product, name='create_product'),
    path('list/', list_products, name='list_products'),
    path('update/<int:product_id>/', update_product, name='update_product'),
    path('delete/<int:product_id>/', delete_product, name='delete_product'),
]
