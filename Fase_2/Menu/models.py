from django.db import models
from django.urls import reverse
import uuid 

# Create your models here.

class Menu(models.Model):
    promociones=models.CharField(max_length=100)
    acompañamientos=models.CharField(max_length=100)
    bebidas=models.CharField(max_length=50)

    def __str__(self):
        return self.promociones

