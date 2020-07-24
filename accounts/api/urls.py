from django.urls import path
from .views import UserListApi


urlpatterns = [
    path('platform/users', UserListApi, name = 'all=users')
]