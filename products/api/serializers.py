from rest_framework import serializers
from ..models import Products
from django.contrib.auth import get_user_model
from ast import literal_eval

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['name', 'price', 'count_stock', 'brand']

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
class ProductAddSerializer(serializers.ModelSerializer):
    userid = serializers.IntegerField()
    prodid = serializers.IntegerField()
    class Meta:
        model = Products
        fields = ['prodid', 'userid']
    def add_to_user(self):
        userid = self.validated_data['userid']
        prodid = self.validated_data['prodid']
        user = get_user_model().objects.get(id = userid)
        prod = Products.objects.get(id = prodid)
        count_check = prod.count_stock 
        user.budget -= int(prod.price)
        if count_check < 1:
            res = "Out of Stock"
            return res
        elif user.budget < 0:
            res = "Your Budget has been exceeded"
            return res
        else:
            user.product_list.add(prod)
            prod.count_stock = count_check - 1
            prod.save()
            user.save()
            return True

class ProductReviewSerializer(serializers.ModelSerializer):
    review = serializers.CharField()
    prodid   = serializers.IntegerField()
    class Meta:
        model = Products
        fields = ['prodid','review']
    
    def review_add(self):
        review = self.validated_data['review']
        prodid = self.validated_data['prodid']
        item = Products.objects.get(id=prodid)
        rlist = literal_eval(item.review_list)
        rlist.append(review)
        rstring = str(rlist)
        item.review_list = rstring
        item.save()

class AllReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['review_list']

class ProductRateSerializer(serializers.ModelSerializer):
    rate = serializers.IntegerField()
    prodid = serializers.IntegerField()
    class Meta:
        model = Products
        fields = [ 'rate', 'prodid']

    def rate_prod(self):
        rate = self.validated_data['rate']
        prodid = self.validated_data['prodid']
        item = Products.objects.get(id=prodid)
        if rate > 0 and rate <= 5:
            new_rating = (item.rating + rate)/2
            item.rating = new_rating
            item.save()
            return True
        else:
            return False

       

