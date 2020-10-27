from django.shortcuts import render, get_object_or_404, redirect
from . models import Menu
from django.views import generic


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