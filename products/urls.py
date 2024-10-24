
from django.urls import path

from . import views


urlpatterns = [
    path('get-products/', views.products,name="wproducts"),
    path('product-details/<int:id>/',views.productDetail,name='productdetail'),

]