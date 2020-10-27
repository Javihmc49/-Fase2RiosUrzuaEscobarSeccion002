from django.db import models
from django.urls import reverse
import uuid 

# Create your models here.

class Menu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    promociones=models.CharField(max_length=100, null=True)
    acompañamientos=models.CharField(max_length=100, null=True)
    bebidas=models.CharField(max_length=50, null=True)
    precio=models.IntegerField(default=1, blank=True, null=True )

    def get_absolute_url(self):
        return reverse('pizza-detail', args=[str(self.id)])

    def __str__(self):
        return self.promociones
