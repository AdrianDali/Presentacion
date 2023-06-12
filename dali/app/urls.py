from django.urls import path, include
from app.views import TestView, CreateCliente, GetCliente, EditCliente, DeleteCliente
from app.views import CreateAdministrador, GetAdministrador, EditAdministrador, DeleteAdministrador
from app.views import CreatePlastico, GetPlastico, EditPlastico, DeletePlastico, InsertPlasticoCliente, GetAllClientes, GetAllClientesPlastico, GetDatosClientes, PDFGeneratorAPIView
urlpatterns = [
    path('test/', TestView.as_view(), name='test'),
    path('createClient/', CreateCliente.as_view(), name='create'),
    path('getClient/', GetCliente.as_view(), name='get'),
    path('getDatosClient/', GetDatosClientes.as_view(), name='get'),

    path('editClient/', EditCliente.as_view(), name='edit'),
    path('createAdministrador/', CreateAdministrador.as_view(), name='delete'),
    path('getAdministrador/', GetAdministrador.as_view(), name='get'),
    path('editAdministrador/', EditAdministrador.as_view(), name='delete'),
    path('deleteAdministrador/', DeleteAdministrador.as_view(), name='delete'),
    path('createPlastico/', CreatePlastico.as_view(), name='delete'),
    path('getPlastico/', GetPlastico.as_view(), name='delete'),
    path('editPlastico/', EditPlastico.as_view(), name='delete'),
    path('deletePlastico/', DeletePlastico.as_view(), name='delete'),
    path('insertClientePlastico/', InsertPlasticoCliente.as_view(), name='delete'),
    path('getAllClientes/', GetAllClientes.as_view(), name='delete'),
    path('getAllClientesPlastico/', GetAllClientesPlastico.as_view(), name='delete'),
    path('pdf/', PDFGeneratorAPIView.as_view(), name='delete'),

]