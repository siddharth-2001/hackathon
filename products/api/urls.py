from django.urls import path
from .views import list_all_products, create_product, view_product

urlpatterns = [
    path("platform/products", list_all_products, name='all-items' ),
    path("platform/products/create", create_product, name='create-item' ),
    path('platform/products/<int:pk>', view_product, name='view-product' ),

]