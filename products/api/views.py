from rest_framework.decorators import api_view
from .serializers import ProductSerializer, ProductCreateSerializer, ProductAddSerializer, ProductReviewSerializer, AllReviewSerializer, ProductRateSerializer
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

@api_view(['PUT'])
def purchase_product(request):
    data = {}
    serializer = ProductAddSerializer(data=request.data)
    if serializer.is_valid():
        check = serializer.add_to_user()
        if check is True:
            data['response'] = "Success"
        else:
            data['response'] = check
    else:
        data['response'] = "Error"
    return Response(data)

@api_view(['PUT'])
def add_review(request):
    data = {}
    serializer = ProductReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.review_add()
        data['response'] = "Success"
    else:
        data['response'] = "Error"
    return Response(data)

@api_view(['GET'])
def get_all_review(request, pk):
    item= Products.objects.get(id=pk)
    serializer = AllReviewSerializer(instance=item)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_product(request,pk):
    item = Products.objects.get(id=pk)
    item.delete()

@api_view(['PUT'])
def rate_product(request):
    data = {}
    serializer = ProductRateSerializer(data = request.data)
    if serializer.is_valid():
        check = serializer.rate_prod()
        if check is True:
            data['response'] = "Successfully rated"
        else:
            data['response'] = "Enter a rating between 0 to 5"
    return Response(data)