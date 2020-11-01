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

class Contacto(models.Model):
    email=models.EmailField()
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    fono=models.IntegerField()
    direccion=models.CharField(max_length=100)
    fecha=models.DateField(auto_now=True)

    motivo_cotacto=[
        ('VentadePizzas', 'Freshman'),
        ('EventosCorporativos', 'Sophomore'),
        ('Alianzas', 'Junior'),
        ('ProblemasConTuPedido', 'Senior'),
        ('Comentarios', 'Graduate'),
    ]

    motivo=models.CharField(max_length=100, choices=motivo_cotacto)

    def __str__(self):
        return self.nombre, self.apellido