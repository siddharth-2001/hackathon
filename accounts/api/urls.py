from django.urls import path
from .views import user_list_api, user_create_api, change_password_api, login_user_api, delete_user, view_product_list
 
app_name = 'accounts'

urlpatterns = [
    path('platform/users', user_list_api, name = 'all-users'),
    path('platform/signup', user_create_api, name = 'sign-up'),
    path('platform/changePassword/<int:pk>', change_password_api, name= 'change-password' ),
    path('platform/login', login_user_api, name='login'),
    path('platform/deleteUser/<int:pk>', delete_user, name = 'delete-user'),
    path('platform/<int:pk>/products',view_product_list, name='list-products')
]