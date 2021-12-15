from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def inicio(request):

    #return HttpResponse('Pagina de inicio')
    return render(request, 'Flotapp/inicio.html')

def misvehiculos(request):

    return render(request, 'Flotapp/mis_vehiculos.html')

def documentacion(request):

    return render(request, 'Flotapp/docs.html')

def nuevoVehiculo(request):

    return render(request, 'Flotapp/nuevo_vehiculo.html')