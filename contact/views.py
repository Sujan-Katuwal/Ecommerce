from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Contact

# Create your views here.

def contact(request):
    return render(request,"contact.html")


def store_contact(request):
    form_email = request.POST['email']
    form_message = request.POST['message']

    #need store in database
    Contact.objects.create(email=form_email,message=form_message)

    messages.success(request, 'Your message saved successfully!')
    return redirect('contact_us')