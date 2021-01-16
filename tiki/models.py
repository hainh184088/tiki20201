from django.db import models
from django.contrib.postgres.fields import JSONField
# Create your models here.
class Category(models.Model):
    idCategory = models.CharField(max_length = 10, primary_key = True)
    name = models.CharField(max_length = 40)
    class Meta: 
        managed = False
        db_table = 'category'

class Seller(models.Model):
    shop_id = models.CharField(max_length = 10, primary_key = True)
    name = models.CharField(max_length = 45)
    logo = models.CharField(max_length = 100)
    class Meta:
        managed = False
        db_table = 'seller'

class Product(models.Model):
    id = models.CharField(max_length = 10, primary_key = True)
    name = models.CharField(max_length = 200)
    url_path = models.CharField(max_length = 200)
    productset_group_name = models.CharField(max_length = 200)
    category = models.ForeignKey(Category, on_delete = models.CASCADE,  related_name='product')
    # min_qty = models.IntegerField()
    # max_qty = models.IntegerField()
    # quantity = models.IntegerField()
    price = models.IntegerField()
    list_price = models.IntegerField()
    discount_rate = models.IntegerField()
    rating_count = models.IntegerField()
    rating_total = models.IntegerField()
    description = models.CharField(max_length = 1000)
    class Meta:
        managed = False
        db_table = 'product'

class Sell(models.Model):
    p = models.OneToOneField(Product,on_delete = models.CASCADE, primary_key = True, related_name = 'sell_product')
    seller = models.OneToOneField(Category,on_delete = models.CASCADE)
    min_qty = models.IntegerField()
    max_qty = models.IntegerField()
    qty = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'sell'

class Image(models.Model):
    product_id = models.OneToOneField(Product,on_delete = models.CASCADE)
    url = models.CharField(max_length = 255, primary_key = True)
    class Meta:
        managed = False
        db_table = 'image'