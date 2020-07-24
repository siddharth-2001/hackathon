from django.urls import path
from .views import UserListApi, UserCreateApi, change_password_api, login_user_api
 
app_name = 'accounts'

urlpatterns = [
    path('platform/users', UserListApi, name = 'all-users'),
    path('platform/signup', UserCreateApi, name = 'sign-up'),
    path('platform/changePassword/<int:pk>', change_password_api, name= 'change-password' ),
    path('platform/login', login_user_api, name='login'),
]