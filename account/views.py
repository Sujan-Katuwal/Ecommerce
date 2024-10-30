from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.
def user_register(request):
    return render(request, 'register.html')

def store_register_user(request):
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('cpassword')
        if password!=confirm_password:
            messages.error(request, 'Password do not match')
        else:
         my_user = User.objects.create_user(username, email, password)
         my_user.save()
         messages.success(request, "User Register Success!!")
         return redirect('user_login')
    

    return render(request, 'register.html')


def user_login(request):
    return render(request, 'login.html')

def store_login_user(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "Login Success!!")
            return redirect('home')
        else:
            messages.error(request, "invalid username or password ")

    return render(request, 'login.html')

