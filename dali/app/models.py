from django.db import models

# Create your models here.

class Administrador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    fecha_ultimo_login = models.DateField()


    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)


    def __str__(self):
        return self.nombre
    
class Plastico(models.Model):
    tipo = models.CharField(max_length=50)
    comentario = models.CharField(max_length=50)
    
    def __str__(self):
        return self.tipo
    
    
class PlasticoCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    plastico = models.ForeignKey(Plastico, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    peso = models.FloatField()
    comentario = models.CharField(max_length=50)

    def __str__(self):
        return self.cliente.nombre + " " + self.plastico.tipo

