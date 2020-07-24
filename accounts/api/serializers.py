from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'contact', 'date_joined', 'budget', 'product_list', 'is_superuser']