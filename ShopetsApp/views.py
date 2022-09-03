from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "ShopetsApp/inicio.html")

def servicios(request):
    return HttpResponse("Servicios")

def tienda(request):
    return HttpResponse("Tienda")

def blog(request):
    return HttpResponse("Blog")

def contacto(request):
    return HttpResponse("Contacto")