from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth import login, authenticate


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

class UpdatePasswordSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(style= {'input_type': 'password'}, write_only= True)
    
    class Meta:
        model = User
        fields = [ 'email', 'new_password']


    def update(self, user):
        new_password = self.validated_data['new_password']
        if self.validated_data['email'] == user.email:
            user.set_password(new_password)
            user.save()
        else:
            print("error")

class LoginUserSerializer(serializers.ModelSerializer):
    username1 = serializers.CharField()
    password1 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['username1', 'password1']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def login(self,request):
        username = self.validated_data['username1']
        password = self.validated_data['password1']
        check = authenticate(username = username, password = password)
        if check is not None:
            login(request, check)
        else:
            print('error')

class UserItemList(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['product_list']