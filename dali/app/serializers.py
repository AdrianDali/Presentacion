from rest_framework import serializers

class ClienteSerializer(serializers.Serializer): 
    nombre = serializers.CharField(max_length=100)
    apellido = serializers.CharField(max_length=100)
    empresa = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100)
    telefono = serializers.CharField(max_length=100)
    direccion = serializers.CharField(max_length=100)

class GetClienteSerializer(serializers.Serializer): 
    empresa = serializers.CharField(max_length=100)

class PlasticoSerializer(serializers.Serializer):
    tipo = serializers.CharField(max_length=100)
    comentario = serializers.CharField(max_length=100)

class GetPlasticoSerializer(serializers.Serializer):
    tipo = serializers.CharField(max_length=100)

class PlasticoClienteSerializer(serializers.Serializer):
    cliente = serializers.CharField(max_length=100)
    plastico = serializers.CharField(max_length=100)
    fecha_inicio = serializers.DateField()
    peso = serializers.FloatField()
    comentario = serializers.CharField(max_length=100)

class GetPlasticoClienteSerializer(serializers.Serializer):
    cliente = serializers.CharField(max_length=100)
    plastico = serializers.CharField(max_length=100)
    fecha_inicio = serializers.DateField()
    peso = serializers.FloatField()
    comentario = serializers.CharField(max_length=100)

class AdministradorSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=100)
    apellido = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100)
    telefono = serializers.CharField(max_length=100)
    direccion = serializers.CharField(max_length=100)
    fecha_nacimiento = serializers.DateField()
    fecha_ultimo_login = serializers.DateField()

class GetAdministradorSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100)