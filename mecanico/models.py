from django.db import models

class Usuario(models.Model):
    RUN = models.IntegerField(primary_key=True)
    DV = models.CharField(max_length=1)
    PNOMBRE = models.CharField(max_length=100)
    SNOMBRE = models.CharField(max_length=100)
    APPATERNO = models.CharField(max_length=100)
    APMATERNO = models.CharField(max_length=100)
    DIRECCION = models.CharField(max_length=300)
    NOM_USUARIO = models.CharField(max_length=100, unique=True)
    CONTRASENA = models.CharField(max_length=100)
    CORREO = models.EmailField(max_length=200)
    NRO_TELEFONICO = models.CharField(max_length=20)
    

class Administrador(models.Model):
    ID_ADMINISTRADOR = models.IntegerField(primary_key=True)
    RUN = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class Servicio(models.Model):
    ID_SERVICIO = models.IntegerField(primary_key=True)
    NOMBRE_SERVICIO = models.CharField(max_length=100)
    DESCRIPCION = models.CharField(max_length=300)
    PRECIO = models.IntegerField()
    IMAGEN = models.ImageField(upload_to='imagenes/',verbose_name="imagen",null=True)



class Cliente(models.Model):
    ID_CLIENTE = models.IntegerField(primary_key=True)
    RUN = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class TipoEmpleado(models.Model):
    ID_TIPO = models.IntegerField(primary_key=True)
    DESC_TIPO = models.CharField(max_length=100)


class Empleado(models.Model):
    ID_EMPLEADO = models.IntegerField(primary_key=True)
    TIPO_EMP = models.ForeignKey(TipoEmpleado, on_delete=models.CASCADE)
    HORAS_TRABAJO = models.IntegerField()
    ID_SERVICIO = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    FEC_CONTRATACION = models.DateTimeField()
    RUN = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class AgendaServicio(models.Model):
    ID_AGEN_SERVICIO = models.IntegerField(primary_key=True)
    ID_SERVICIO = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    ID_EMPLEADO = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    ID_CLIENTE = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    FECHA_AGENDADA = models.DateTimeField()


class Proveedor(models.Model):
    ID_PROVEEDOR = models.IntegerField(primary_key=True)
    NOMBRE_PROV = models.CharField(max_length=50)
    DIRECCION = models.CharField(max_length=100)
    CORREO = models.EmailField(max_length=50)
    NRO_TELEFONO =  models.CharField(max_length=20)
    RUBRO = models.CharField(max_length=50)


class Producto(models.Model):
    ID_PRODUCTO = models.IntegerField(primary_key=True)
    NOM_PRODUCTO = models.CharField(max_length=100)
    DESCRIPCION = models.CharField(max_length=300)
    PRECIO = models.IntegerField()
    ID_PROVEEDOR = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    IMAGEN = models.ImageField(upload_to='imagenes/',verbose_name="imagen",null=True)



class Compra(models.Model):
    ID_COMPRA = models.IntegerField(primary_key=True)
    ID_EMPLEADO = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    ID_CLIENTE = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    ID_PRODUCTO = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True)
    ID_SERVICIO = models.ForeignKey(Servicio, on_delete=models.CASCADE, null=True, blank=True)
    TOTAL = models.IntegerField()
    TIPO_COMPRA = models.CharField(max_length=20)
    NRO_BOLETA = models.CharField(max_length=20,null=True)
    NRO_FACTURA = models.CharField(max_length=20,null=True)
    ID_AGEN_SERVICIO = models.ForeignKey(AgendaServicio, on_delete=models.CASCADE,null=True)



class Pedido(models.Model):
    ID_PEDIDO = models.IntegerField(primary_key=True)
    DIRECCION = models.CharField(max_length=100)
    ESTADO = models.CharField(max_length=50)
    ID_COMPRA = models.ForeignKey(Compra, on_delete=models.CASCADE)


class Informe(models.Model):
    ID_INFORME = models.IntegerField(primary_key=True)
    ID_COMPRA = models.ForeignKey(Compra, on_delete=models.CASCADE)
    FECHA = models.DateField()


