from rest_framework import serializers
from tiki.models import Category, Seller, Sell, Image, Product, User
class SellerSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Seller
        fields = ['shop_id','name','logo']
        # fields = "__all__"        fields = "__all__"
class SellSerializer(serializers.ModelSerializer):
    # p = ProductSerializer(many = True, required = True)
    seller_set = SellerSerializer(many = True, read_only = True)
    class Meta:
        model = Sell
        fields = ['seller_set','p_id','seller_id','min_qty','max_qty','qty']
class ProductSerializer(serializers.ModelSerializer):
    sell_set = SellSerializer(many = True, read_only = True)
    class Meta:
        model = Product
        fields = ['sell_set','id','name','url_path','short_description','thumbnail_url','productset_group_name','price','list_price','discount_rate','rating_count','rating_total','description']
class CategoryProductSerializer(serializers.ModelSerializer):
    product_set = ProductSerializer(many = True, read_only = True)
    class Meta: 
        model = Category
        fields = ['id_category','name', 'product_set']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"





class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = "__all__"