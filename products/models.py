from django.db import models

class Banner(models.Model):
    banner = models.ImageField(upload_to="banner")



# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    

class Products(models.Model):
    name=models.CharField(max_length=200)
    price = models.IntegerField()
    discount = models.IntegerField()
    image = models.ImageField(upload_to = 'image/')
    description = models.TextField()

    def __str__(self) -> str:
     return self.name


