from django.urls import path
from .views import UserListApi, UserCreateApi
 
app_name = 'accounts'

urlpatterns = [
    path('platform/users', UserListApi, name = 'all-users'),
    path('platform/signup', UserCreateApi, name = 'sign-up'),
]