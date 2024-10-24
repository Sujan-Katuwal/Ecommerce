from django.shortcuts import render,redirect
from .models import MyUser
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login


# Create your views here.
def user_register(request):
   return render(request, "register.html")
   

def user_store(request):
    if request.POST:
     username = request.POST['username']
     email = request.POST['email']
     password = request.POST['password']
     phone = request.POST['phone']
     MyUser.objects.create(username=username, email=email, password=password, phone=phone)
     messages.success(request, "User Register Success")

     return render(request, "login.html")
    
def user_login(request):
   return render(request, "login.html")

def login_user_store(request):
    if request.POST:
     email = request.POST['email']
     password = request.POST['password']
     try:
       # Find the user based on the email
      user = MyUser.objects.get(email=email)
     except MyUser.DoesNotExist:
        messages.error(request, "No user with this email exists.")
        return render(request, "login.html")
      # Authenticate using the username and password
     user = authenticate(request, email=user.email, password=password)
     if user is not None:
        # Successful authentication
            auth_login(request, user)
            return redirect('home')
     else:
        # Password does not match
            messages.error(request, "The password is incorrect.")
            return render(request, "login.html")
    else:
       return render(request, "login.html")


     
   