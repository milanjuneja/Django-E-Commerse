from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View


class Signup(View):

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email,
        }

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)

        error_message = self.validateCustomer(customer)

        if (not error_message):
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('home')

        else:
            data = {
                'error': error_message,
                'values': value,
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None

        if (not customer.first_name):
            error_message = "First Name Required..!!"
        elif len(customer.first_name) < 4:
            error_message = 'First Name must me 4 Character Long'
        elif not customer.last_name:
            error_message = 'Last name required'
        elif len(customer.last_name) < 4:
            error_message = 'must me 4 character long'
        elif not customer.phone:
            error_message = 'Phone number required'
        elif len(customer.phone) < 10:
            error_message = 'Number should be of 10 digit'
        elif not customer.password:
            error_message = 'Password required'
        elif len(customer.password) < 6:
            error_message = 'Password Should me 6 character or more'
        elif customer.isExist():
            error_message = 'Email Already Exists'
        return error_message
