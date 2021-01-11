from django.shortcuts import render
from store.models.product import Product
from django.views import View
from django.http import HttpResponse


class Cart(View):

    def get(self, request):
        cart = request.session.get('cart')

        if cart:
                
            ids = list(request.session.get('cart').keys())
            if ids:
                products = Product.get_product_by_id(ids)
                print(products)
                return render(request, 'cart.html', {'products': products})
            else:
                return render(request, 'cart.html')
        else:
            request.session.cart={}        
            
            return render(request, 'cart.html')