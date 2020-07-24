from rest_framework.decorators import api_view
from .serializers import ProductSerializer, ProductCreateSerializer
from ..models import Products
from rest_framework.response import Response


@api_view(['GET'])
def list_all_products(request):
    items = Products.objects.all()
    serializer = ProductSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_product(request):
    serializer = ProductCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def view_product(request,pk):
    item = Products.objects.get(id = pk)
    serializer = ProductCreateSerializer(instance=item)
    return Response(serializer.data)