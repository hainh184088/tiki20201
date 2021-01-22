from rest_framework import serializers
from tiki.models import Category, Seller, Sell, Image, Product
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"
class CategoryProductSerializer(serializers.ModelSerializer):
    product_set = ProductSerializer(many = True, read_only = True)
    class Meta: 
        model = Category
        fields = ['id_category','name', 'product_set']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class SellerSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Seller
        fields = "__all__"

class SellSerializer(serializers.ModelSerializer):
    # p = ProductSerializer(many = True, required = True)
    # seller = CategorySerializer(required = True)
    class Meta:
        model = Sell
        fields = "__all__"