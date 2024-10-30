from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.user_register, name="user_register"),
    path('login/', views.user_login, name="user_login"),
    path('store_register_user/', views.store_register_user, name="store_register_user"),
    path('store_login_user/', views.store_login_user, name="store_login_user"),

]