from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def inicio(request):

    #return HttpResponse('Pagina de inicio')
    return render(request, 'Flotapp/inicio.html')

def flota(request):

    #return HttpResponse('tablero de móviles')
    return render(request, 'Flotapp/flota.html')

def documentacion(request):

    #return HttpResponse('tablero de documentación')
    return render(request, 'Flotapp/docs.html')