from django.core import paginator
from django.shortcuts import render, redirect

from store.models.product import Product
from store.models.category import Category
from django.views import View
from django.core.paginator import Paginator


class Index(View):
    def get(self, request):
        # no_of_products = 6
        # page = request.GET.get('page')
        # if page is None:
        #     page = 1
        # else:
        #     page = int(page)
        # print(page)

        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}


        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_product_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()
            paginator = Paginator(products,5)
            page_number = request.GET.get('page',1)
            page_obj = paginator.get_page(page_number)
        data = {}
        data['products'] = page_obj.object_list
        data['categories'] = categories
        data['paginator'] = paginator
        data['page_number'] = int(page_number)
        return render(request, 'index.html', data)

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart

        return redirect('home')
