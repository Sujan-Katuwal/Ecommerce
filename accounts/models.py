from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class MyUser(models.Model):
    username=models.CharField(max_length=120)
    email=models.EmailField(max_length=120)
    password=models.CharField(max_length=120)
    phone_regex = RegexValidator(
        regex=r'^\d{10}$',
        message="Phone number must be exactly 10 digits."
    )
    phone=models.CharField(validators=[phone_regex], max_length=10, blank=False)