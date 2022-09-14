from django.shortcuts import render, HttpResponse
from servicios.models import Servicio

# Create your views here.

def inicio(request):
    return render(request, "ShopetsApp/inicio.html")

def tienda(request):
    return render(request, "ShopetsApp/tienda.html")

def blog(request):
    return render(request, "ShopetsApp/blog.html")

def contacto(request):
    return render(request, "ShopetsApp/contacto.html")