from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.CharField(max_length = 1200)
    message = models.TextField()

    def __str__(self) -> str:
        return self.message
