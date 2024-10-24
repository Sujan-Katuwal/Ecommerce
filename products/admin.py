from django.contrib import admin
from .models import Products,Category,Banner



from .models import Products
# Register your models here.
admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Banner)
