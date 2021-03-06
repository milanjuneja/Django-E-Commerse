from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, default = 1,on_delete=models.CASCADE)
    desc = models.TextField(max_length=2000, default='', null=True, blank=True)
    image = models.ImageField(upload_to='uploads/products')


    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in=ids)
    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_product_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()

    @staticmethod
    def get_product_by_product_id(product_id):
        if product_id:
            return Product.objects.filter(category = product_id)
        else:
            return Product.get_all_products()