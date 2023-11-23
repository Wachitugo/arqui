from django.db import models

# Create your models here.
class USUARIO(models.Model):
    rut = models.CharField( max_length=9,primary_key=True)
    nombre = models.CharField(max_length=30,blank=False,null=False, unique=True)
    contra = models.CharField(max_length=30,blank=False,null=False)
    id_ciudad = models.ForeignKey('Ciudad',on_delete=models.CASCADE, db_column='idciudad')
    saldo = models.CharField(max_length=6)
    correo = models.CharField(max_length=50)
    def __str__(self):
        return str(self.rut)

class CIUDAD(models.Model):
    id_ciudad  = models.AutoField(db_column='idciudad', primary_key=True) 
    nombre_ciudad = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.nombre_ciudad)

    

