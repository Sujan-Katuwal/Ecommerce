
from django.shortcuts import render
# from products.models import Products
from adminPanel.models import Product

# Create your views here.

def products(request):
    data = {'title':"Daraz Ecom | product page dynamic title"}
    all_products = Product.objects.all()
    data = {
        'products': all_products
    }
    return render(request,"product.html",data)

def productDetail(request, id):
     single_product = Product.objects.filter(id=id).first()
     data = {
        'product':single_product,
     }
     return render(request, "product_details.html", data)

