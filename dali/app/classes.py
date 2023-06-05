from app.models import Cliente as ClienteModel, Plastico as PlasticoModel, Administrador as AdministradorModel, PlasticoCliente as PlasticoClienteModel

class Administrador:
    def __init__(self,data) -> None:
        self.data = data
        self.nombre = data.get("nombre")
        self.apellido = data.get("apellido")
        self.email = data.get("email")
        self.password = data.get("password")
        self.telefono = data.get("telefono")
        self.direccion = data.get("direccion")
        self.fecha_nacimiento = data.get("fecha_nacimiento")
        self.fecha_ultimo_login = data.get("fecha_ultimo_login")

    def insert_db(self):
        try:
            administrador = AdministradorModel.objects.create(
                nombre = self.nombre,
                apellido = self.apellido,
                email = self.email,
                password = self.password,
                telefono = self.telefono,
                direccion = self.direccion,
                fecha_nacimiento = self.fecha_nacimiento,
                fecha_ultimo_login = self.fecha_ultimo_login
            )
            administrador.save()
        except Exception as e:
            print(e)
            return None
        
        return administrador

class Plastico:
    def __init__(self, data) -> None:
        self.data = data
        self.tipo = data.get("tipo")
        self.comentario = data.get("comentario")

    def insert_db(self):
        try:
            plastico = PlasticoModel.objects.create(
                tipo = self.tipo,
                comentario = self.comentario
            )
            plastico.save()
        except Exception as e:
            print(e)
            return None
        
        return plastico


class Cliente: 
    def __init__(self, data) -> None:
        self.data = data
        self.nombre = data.get("nombre")
        self.apellido = data.get("apellido")
        self.empresa = data.get("empresa")
        self.email = data.get("email")
        self.password = data.get("password")
        self.telefono = data.get("telefono")
        self.direccion = data.get("direccion")


    def insert_db(self):
        try:
            cliente = ClienteModel.objects.create(
                nombre = self.nombre,
                apellido = self.apellido,
                empresa = self.empresa,
                email = self.email,
                password = self.password,
                telefono = self.telefono,
                direccion = self.direccion
            )
            cliente.save()
        except Exception as e:
            print(e)
            return None
        
        return cliente

class PlasticoCliente: 
    def __init__(self, data) -> None:
        self.data = data
        self.cliente = data.get("cliente")
        self.plastico = data.get("plastico")
        self.fecha_inicio = data.get("fecha_inicio")
        self.peso = data.get("peso")
        self.comentario = data.get("comentario")

    def insert_db(self):
        try:
            plastico_cliente = PlasticoClienteModel.objects.create(
                cliente = ClienteModel.objects.get(nombre=self.cliente),
                plastico = PlasticoModel.objects.get(tipo=self.plastico),
                fecha_inicio = self.fecha_inicio,
                peso = self.peso,
                comentario = self.comentario
            )
            plastico_cliente.save()
        except Exception as e:
            print(e)
            return None
        
        return plastico_cliente


