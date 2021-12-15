from django.urls import path
from Flotapp import views

urlpatterns = [
    
    path('', views.inicio),

    path('mis_vehiculos', views.misvehiculos),

    path('service', views.service),

    path('nuevo_vehiculo', views.nuevoVehiculo),

    path('home', views.home),

]