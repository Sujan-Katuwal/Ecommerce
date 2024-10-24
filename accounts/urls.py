from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.user_register, name="user_register"),
    path('user_store/', views.user_store, name="user_store"),
    path('login/', views.user_login, name="user_login"),
    path('login_user_store/', views.login_user_store, name="login_user_store")
   
]