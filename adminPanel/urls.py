from django.urls import path

from . import views

urlpatterns = [
    path('admin_index/', views.admin_index, name="admin_index"),
    path('admin_product/', views.admin_product, name="admin_product"),
    path('admin_add_category/', views.admin_add_category, name='admin_add_category'),
    path("admin_add_category_validation/", views.admin_add_category_validation, name = "admin_add_category_validation"),
    path("admin_add_product/", views.admin_add_product, name = "admin_add_product"),
    path("admin_add_product_validation/", views.admin_add_product_validation, name = "admin_add_product_validation"),
    path("admin_login/", views.admin_login, name = "admin_login"),
    path("logout/", views.admin_logout, name="admin_logout"),
    path("admin_account/", views.admin_account, name = "admin_account"),
    path("delete_product/<int:id>", views.delete_product, name="delete_product"),
    path("delete_category/<int:id>", views.delete_category, name="delete_category"),
   
    
]