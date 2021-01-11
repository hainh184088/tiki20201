from rest_framework import serializers
from tiki.models import Category, Seller, Sell, Image, Product
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Category
        fields = "__all__"
class SellerSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Seller
        fields = "__all__"
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only = True)
    class Meta:
        model = Product
        fields = "__all__"