from django.db import models
from django.db.models.base import Model

# Create your models here.

class movil(models.Model):

    tipo = models.CharField(max_length=30)
    dominio = models.CharField(max_length=10)
    conductores = models.IntegerField()
    