from rest_framework import serializers
from tiki.models import Category, Seller, Sell, Image, Product
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    product = ProductSerializer(many = True, read_only = True)
    class Meta: 
        model = Category
        fields = ['id_category','name', 'product']
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