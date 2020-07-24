from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'contact', 'date_joined', 'budget', 'product_list', 'is_superuser']

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'contact','budget', 'password']
        extra_kwargs = {
            'password' : {'write_only': True}
        }

    def save(self):
        account = User.objects.create(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
            contact = self.validated_data['contact'],
            budget = self.validated_data['budget'],
        )
        password = self.validated_data['password']
        account.set_password(password)
        print(account)
        account.save()
        return account