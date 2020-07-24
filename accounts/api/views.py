from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserListSerializer


@api_view(['GET'])
def UserListApi(request):
    user_class = get_user_model()
    User = user_class.objects.all()
    serializer = UserListSerializer(User, many = True)
    return Response(serializer.data)