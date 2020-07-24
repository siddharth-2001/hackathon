from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserListSerializer, UserCreateSerializer, UpdatePasswordSerializer, LoginUserApi
from rest_framework.authtoken.models import Token


@api_view(['GET'])
def UserListApi(request):
    User = get_user_model().objects.all()
    serializer = UserListSerializer(User, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def UserCreateApi(request):
    data = {}
    serial = UserCreateSerializer(data=request.data)
    if serial.is_valid():
        user = serial.save()
        data['username'] = user.username
        data['email'] = user.email
        data['response'] = "You have been successfully registered"
    else:
        data['response'] = "Some error has occurred"
    return Response(data)
@api_view(['PUT'])
def change_password_api(request):
    data = {}
    user = get_user_model().objects.get(id= pk )
    serializer = UpdatePasswordSerializer(instance = user, data = request.data) 
    if serializer.is_valid():
        serializer.update(user)
        data['response'] = "You have successfully changed your password"
    else:
        data['response'] = "Some error has occurred"
        print(serializer.errors)
    return Response(data)
@api_view(['POST'])
def login_user_api(request):
    data = {}
    serializer = LoginUserApi(data=request.data)
    if serializer.is_valid():
        serializer.login(request)
        tok_check = list(Token.objects.filter(user=request.user))
        if len(tok_check) == 0 :
            token = Token.objects.create(user=request.user)
        else:
            token = Token.objects.get(user=request.user)
        data['response'] = "You have successfully logged in"
        data['token'] = token.key
        print(request.user)
    else:
        print(serializer.errors)
        data['response'] = "Some errorr has occurred"
    return Response(data)
    