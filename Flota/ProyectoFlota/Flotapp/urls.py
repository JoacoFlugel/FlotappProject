from django.urls import path
from Flotapp import views

urlpatterns = [
    
    path('', views.inicio),

    path('flota', views.flota),

    path('documents', views.documentacion)

]