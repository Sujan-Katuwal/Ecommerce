
from django.shortcuts import render, redirect
from django.http import HttpResponse
from products.models import Banner
from adminPanel.models import Product

def home(request):
     # data = {'titles':"eShop | Home page "}
     banner = Banner.objects.all()
     product = Product.objects.all()
     data = {
        'banners':banner,
        'Products':Product,
    }
     return render(request, "index.html", data)

def product(request):
     # data = {'title':"eShop | product page "}
     my_Product = Product.objects.all()
     # data = {
     #      'Products':Product,
     # }
     return render(request, "product.html", {'my_Product' : my_Product})