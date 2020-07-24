from rest_framework import serializers
from ..models import Products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['name', 'price', 'count_stock', 'brand']

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
