from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from app.serializers import ClienteSerializer, GetClienteSerializer, PlasticoSerializer, GetPlasticoSerializer, PlasticoClienteSerializer, GetPlasticoClienteSerializer, AdministradorSerializer, GetAdministradorSerializer
from app.classes import Cliente, Plastico, Administrador, PlasticoCliente
from app.models import Cliente as ClienteModel , Administrador as AdministradorModel, Plastico as PlasticoModel, PlasticoCliente as PlasticoClienteModel
from rest_framework.exceptions import APIException
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from io import BytesIO
from reportlab.lib.units import inch
from reportlab.platypus import Image
from django.conf import settings
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


# Create your views here.
class TestView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        return HttpResponse("Hello, World!")
    
class CreateAdministrador(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        serializer = AdministradorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        print(data)
        administrador = Administrador(data)
        try:
            administrador.insert_db()
            print("Administrador creado con exito")
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
        return Response(status=status.HTTP_201_CREATED)

class GetAdministrador(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        serializer = GetAdministradorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        print(data)

        if not AdministradorModel.objects.filter(email=data.get("email")).exists():
            raise APIException(
                'No existe un administrador registrado con este email'
            )
        administrador = AdministradorModel.objects.get(email=data.get("email"))
        print(administrador)
        return Response(status=status.HTTP_200_OK)

class EditAdministrador(APIView):
    permission_classes = (AllowAny,)
    def put(self, request):
        serializer = AdministradorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        print(data)

        if not AdministradorModel.objects.filter(email=data.get("email")).exists():
            raise APIException(
                'No existe un administrador registrado con este email'
            )
        administrador = AdministradorModel.objects.get(email=data.get("email"))
        administrador.nombre = data.get("nombre")
        administrador.apellido = data.get("apellido")
        administrador.empresa = data.get("empresa")
        administrador.email = data.get("email")
        administrador.password = data.get("password")
        administrador.telefono = data.get("telefono")
        administrador.direccion = data.get("direccion")
        administrador.save()
        print(administrador)
        return Response(status=status.HTTP_200_OK)

class DeleteAdministrador(APIView):
    permission_classes = (AllowAny,)
    def delete(self, request):
        serializer = GetAdministradorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        print(data)

        if not AdministradorModel.objects.filter(email=data.get("email")).exists():
            raise APIException(
                'No existe un administrador registrado con este email'
            )
        administrador = AdministradorModel.objects.get(email=data.get("email"))
        administrador.delete()
        print(administrador)
        return Response(status=status.HTTP_200_OK)

    
class CreateCliente(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        serializer = ClienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        print(data)
        cliente = Cliente(data)
        try:
            cliente.insert_db()
            print("Cliente creado con exito")
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
        return Response(status=status.HTTP_201_CREATED)
    
class GetCliente(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        serializer = GetClienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        print(data)

        if not ClienteModel.objects.filter(empresa=data.get("empresa")).exists():
            raise APIException(
                'No existe un cliente registrado con esta empresa')

        cliente = ClienteModel.objects.get(empresa=data.get("empresa"))

        return Response(data={"empresa": cliente.nombre,}, status=status.HTTP_200_OK)

class GetDatosClientes(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        Clientes = ClienteModel.objects.all()
        serializer = ClienteSerializer(Clientes, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
        




class EditCliente(APIView):
    permission_classes = (AllowAny,)
    def put(self, request):
        seerializer = ClienteSerializer(data=request.data)
        seerializer.is_valid(raise_exception=True)
        data = seerializer.validated_data
        print(data)
        cliente = Cliente(data)

        serializer = ClienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        print("CLiente#################################")
        print(data)
        clienteNuevo = Cliente(data)

        if ClienteModel.objects.filter(empresa = cliente.empresa).exists():
            clienteModel = ClienteModel.objects.get(empresa = cliente.empresa)
            clienteModel.nombre = clienteNuevo.nombre
            clienteModel.apellido = clienteNuevo.apellido
            clienteModel.empresa = clienteNuevo.empresa
            clienteModel.email = clienteNuevo.email
            clienteModel.password = clienteNuevo.password
            clienteModel.telefono = clienteNuevo.telefono
            clienteModel.direccion = clienteNuevo.direccion
            clienteModel.save()
            print("Cliente editado con exito")

        return Response(data= {"message": "Cliente actualizado"},status=status.HTTP_200_OK)

class DeleteCliente(APIView):
    permission_classes = (AllowAny,)
    def delete(self, request):
        serializer = GetClienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        print(data)
        cliente = Cliente(data)

        if ClienteModel.objects.filter(empresa = cliente.empresa).exists():
            try:
                clienteModel = ClienteModel.objects.get(empresa = cliente.empresa)
                clienteModel.delete()
                print("Cliente eliminado con exito")
                return Response(status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else: 
            print("No existe el cliente")
            return Response(status=status.HTTP_400_BAD_REQUEST)


        
    
class CreatePlastico(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        serializer = PlasticoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        print(data)
        plastico = Plastico(data)
        try:
            plastico.insert_db()
            print("Plastico creado con exito")
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)

class GetPlastico(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        serializer = GetPlasticoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        print(data)

        if not Plastico.objects.filter(id=data.get("id")).exists():
            raise APIException(
                'No existe un plastico registrado con este id')

        plastico = Plastico.objects.get(id=data.get("id"))

        return Response(data={"id": plastico.id, "nombre": plastico.nombre, "precio": plastico.precio, "cantidad": plastico.cantidad, "color": plastico.color}, status=status.HTTP_200_OK)
    
class EditPlastico(APIView):
    permission_classes = (AllowAny,)
    def put(self, request):
        seerializer = PlasticoSerializer(data=request.data)
        seerializer.is_valid(raise_exception=True)
        data = seerializer.validated_data
        print(data)
        plastico = Plastico(data)

        serializer = PlasticoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        print("Plastico#################################")
        print(data)
        plasticoNuevo = Plastico(data)

        if Plastico.objects.filter(id = plastico.id).exists():
            plasticoModel = Plastico.objects.get(id = plastico.id)
            plasticoModel.nombre = plasticoNuevo.nombre
            plasticoModel.precio = plasticoNuevo.precio
            plasticoModel.cantidad = plasticoNuevo.cantidad
            plasticoModel.color = plasticoNuevo.color
            plasticoModel.save()
            print("Plastico editado con exito")

        return Response(data= {"message": "Plastico actualizado"},status=status.HTTP_200_OK)
    
class DeletePlastico(APIView):
    permission_classes = (AllowAny,)
    def delete(self, request):
        serializer = GetPlasticoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        print(data)
        plastico = Plastico(data)

        if Plastico.objects.filter(id = plastico.id).exists():
            try:
                plasticoModel = Plastico.objects.get(id = plastico.id)
                plasticoModel.delete()
                print("Plastico eliminado con exito")
                return Response(status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else: 
            print("No existe el plastico")
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class InsertPlasticoCliente(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):  
        serializer = PlasticoClienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        print(data)
        plasticoCliente = PlasticoCliente(data)

        try:
            plasticoCliente.insert_db()
            print("PlasticoCliente creado con exito")
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(e)

            return Response(status=status.HTTP_400_BAD_REQUEST)

class GetAllClientes (APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        clientes = ClienteModel.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)


class GetAllClientesPlastico (APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        clientes = ClienteModel.objects.all()
        clientesPlastico = PlasticoClienteModel.objects.all()
        serializer = PlasticoClienteSerializer(clientesPlastico, many=True)
        plastico = 0
        listaClientes = []
        listaPesoClientes = []
        for cliente in clientes:
            listaClientes.append(cliente.nombre)
            for clientePlastico in clientesPlastico:
                if cliente.nombre == clientePlastico.cliente.nombre:
                    plastico += clientePlastico.peso
            

            listaPesoClientes.append(plastico)


            plastico = 0

        total = 0
        index = 0
        for i in listaPesoClientes:
            index += 1
            total += i
        listaPorcentaje = []
        for i in listaPesoClientes:
            print("##########WQEDSDASDASDASDAS")
            print(total)
            listaPorcentaje.append((int(i)*100)//total)


       

        return Response(data={"clientes": listaClientes, "pesos": listaPorcentaje}, status=status.HTTP_200_OK)
            

class PDFGeneratorAPIView(APIView):
    def get(self, request, format=None):
        # Crear el objeto BytesIO para almacenar el PDF generado en memoria
        buffer = BytesIO()

        # Crear el objeto del documento PDF con margen de 1 pulgada
        doc = SimpleDocTemplate(buffer, pagesize=letter, leftMargin=inch, rightMargin=inch,
                                topMargin=inch, bottomMargin=inch)

        # Datos para la tabla
        data = [
            ['RFC:', '','Razón Social:'],
            [''],
            ['Domicilio:' , ''],
            [''],
            ['Calle:' , '','Numero:', '', 'C.P:'],
            [''],
            ['Colonia:', '', 'Alcaldia:', ''],
            [''],
            ['Estado:', '', 'Contacto:', ''],
            [''],
            ['', '', 'Telefono:', ''],
            [''],
            [''],
            ['Recoleccion', '','Disposicion','','Ruta','','Procedencia:'],
            [''],
            ['Ubicacion:', ''],
            [''],
            [''],
            [''],
            ['Tipo de Residuos:','', 'Cantidad:',''],

            

            
        ]

        # Crear la tabla y establecer el estilo
        table = Table(data)
        style = TableStyle([
            # Establecer los estilos de la tabla aquí (como se mostró anteriormente)
            ('BACKGROUND', (0, 0), (-1, 0), colors.black),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),

            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),

            ('BACKGROUND', (0, 1), (-1, 15), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, 1), colors.black),
            ('FONTNAME', (0, 1), (-1, 1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, 1), 10),
            ('ALIGN', (0, 1), (-1, 1), 'LEFT'),
            ('BOTTOMPADDING', (0, 1), (-1, 1), 12),




            

        ])
        table.setStyle(style)

        # Crear el flujo de elementos y agregar la tabla
        elements = []
        styles = getSampleStyleSheet()

                # Agregar texto en la parte superior derecha
        texto_fuera_de_tabla = "Datos del Generador"
        estilo_fuera_de_tabla = ParagraphStyle('FueraDeTabla', parent=styles['Normal'], alignment=0, fontSize=12)
        texto_paragraph = Paragraph(texto_fuera_de_tabla, estilo_fuera_de_tabla)
        elements.append(texto_paragraph)

        elements.append(table)



        # Generar el documento PDF
        doc.build(elements)


        # Obtener el contenido del PDF desde el objeto BytesIO
        pdf = buffer.getvalue()
        buffer.close()

        # Crear el objeto HttpResponse con el tipo de contenido PDF.
        response = HttpResponse(content_type='application/pdf')

        # Establecer el nombre del archivo PDF.
        response['Content-Disposition'] = 'attachment; filename="ejemplo.pdf"'

        # Escribir el contenido del PDF en el objeto HttpResponse
        response.write(pdf)

        return response



