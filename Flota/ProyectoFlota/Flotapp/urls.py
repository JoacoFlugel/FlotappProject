from django.urls import path
from Flotapp import views

urlpatterns = [
    
    path('', views.inicio),

    path('mis_vehiculos', views.misvehiculos),

    path('documents', views.documentacion)

]