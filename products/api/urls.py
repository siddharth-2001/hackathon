from django.urls import path
from .views import list_all_products, create_product, view_product, purchase_product, add_review, get_all_review, delete_product, rate_product

urlpatterns = [
    path("platform/products", list_all_products, name='all-items' ),
    path("platform/products/create", create_product, name='create-item' ),
    path('platform/products/<int:pk>', view_product, name='view-product' ),
    path('platform/products/purchase', purchase_product, name='add-prod'),
    path('platform/products/review', add_review, name='add-review'),
    path('platform/products/<int:pk>/reviews', get_all_review, name='all-review'),
    path('platform/deleteProduct/<int:pk>', delete_product, name = 'del-product'),
    path('platform/products/rate', rate_product, name = 'rate'),

]