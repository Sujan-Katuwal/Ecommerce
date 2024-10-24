from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='categories/images/', null = True)


    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length = 2000)
    price = models.IntegerField()
    discount = models.IntegerField()
    image = models.ImageField(upload_to='products/images/', null = True, max_length=250, default=None)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)

    def __str__(self)  -> str:
        return self.name