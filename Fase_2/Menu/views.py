from django.shortcuts import render, get_object_or_404, redirect
from . models import Menu,Contacto
from django.views import generic
from django.http import HttpResponse


# Create your views here.

def index(request):
    num = Menu.objects.all()

    return render(
        request,
        'index.html',
        context={'num':num}
    )

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
class PizzaDetalles(generic.DetailView):
    model = Menu


def contacto(request):
    if request.method=="POST":
        contacto=Contacto()
        nombre=request.POST.get('nombre')
        email=request.POST.get('email')
        apellido=request.POST.get('apellido')
        fono=request.POST.get('fono')
        direccion=request.POST.get('direccion')
        fecha=request.POST.get('fecha')
        motivo=request.POST.get('motivo')

        contacto.nombre=nombre
        contacto.email=email
        contacto.apellido=apellido
        contacto.fono=fono
        contacto.direccion=direccion
        contacto.motivo=motivo
        contacto.save()
        return HttpResponse("<h1>GRACIAS POR CONTACTARNOS</h1>")
    return render(request,'Contacto.html')

def sobre_nosotros(request):
    return render(request,'Sobre_Nosotros.html')