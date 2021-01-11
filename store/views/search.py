from django.db.models import query
from django.shortcuts import render, redirect

from store.models.product import Product
from store.models.category import Category
from django.views import View

class Search(View):
    def post(self, request):
        return render(request, 'search.html')
    def get(self, request):
        query = request.GET['query']
        
        categories = Category.get_all_categories()
        products_name = Product.objects.filter(name__icontains=query)
        products_desc =Product.objects.filter(desc__icontains=query)
        products  = products_name.union(products_desc)
        data = {}
        data['products'] = products
        data['categories'] = categories
        data['query'] = query
        return render(request, 'search.html', data)   

