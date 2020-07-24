from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserListSerializer, UserCreateSerializer


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