
from django.urls import path

from . import views


urlpatterns = [
    path('contact-us/', views.contact,name="contact_us"),
    path('contact-store-contact/',views.store_contact,name="store_contact_us"),
    

]