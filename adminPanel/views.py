from django.shortcuts import render, redirect
from .models import Category, Product
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='admin/admin_login/')
def admin_index(request):
    return render(request, "adminindex.html")

# @login_required(login_url='admin/admin_login/')
def admin_product(request):
    all_categories = Category.objects.all()
    all_product = Product.objects.all()
    data = {
        "categories": all_categories,
        "products": all_product,
        "active_page": 'product'
    }
    return render(request, "adminproduct.html", data)


def admin_add_category(request):
    return render(request, "adminAddCategory.html")

def admin_add_category_validation(request):
    category_name = request.POST['c_name']
    category_image = request.FILES['c_image']

    Category.objects.create(name=category_name, image=category_image)

    messages.success(request, "Category added Successfully")

    return redirect('admin_add_category')

# @login_required(login_url='admin/admin_login/')
def admin_add_product(request):
    category_list = Category.objects.all()

    return render(request, "adminAddProduct.html", {"show_category":category_list} )

def admin_add_product_validation(request):
    if request.POST:
        product_name = request.POST['p_name']
        product_price = request.POST['p_price']
        product_discount = request.POST['p_discount']
        product_image = request.FILES['p_image']
        product_description = request.POST['p_description']
        product_category = request.POST['p_category']
        product_stock = request.POST['p_stock']
        
        Product.objects.create(name=product_name, price=product_price, discount=product_discount, image= product_image, description=product_description, category_id=product_category, stock=product_stock)

        messages.success(request, "Product added Successfully")


        return redirect("admin_add_product")

def delete_product(request, id):
    delete_product = Product.objects.get(id=id)
    delete_product.delete()
    messages.success(request, "Product deleted Successfully")

    return render(request, "adminAddProduct.html")

def delete_category(request, id):
    delete_category = Category.objects.get(id=id)
    delete_category.delete()
    messages.success(request, "Category Deleted Successfully")

    return render(request, "adminAddProduct.html")
    
def admin_login(request):
    if request.method == "POST":
         #here will be login process
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Login Successfully")
            return redirect('admin_index')
        else:
            print("data get failed")
            return render(request, "adminLogin.html", {"error": "Invalid username or password"})
    else:
        return render(request, "adminLogin.html")

    

def admin_logout(request):
    logout(request)
    return redirect(admin_login)

def admin_account(request):
    return render(request, "adminAccounts.html")
    