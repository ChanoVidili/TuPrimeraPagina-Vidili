from django.db import models

# Create your models here.

class Club(models.Model):
    nombre = models.CharField(max_length=40)
    fundacion = models.IntegerField()
    
    def __str__(self):
        return self.nombre
    
class Jugador(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    pierna_habil = models.CharField(max_length=40)
    
    def __str__(self):
        return self.apellido
    
class Director_Tecnico(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    tactica_preferida = models.CharField(max_length=30)
    
    def __str__(self):
        return self.apellido