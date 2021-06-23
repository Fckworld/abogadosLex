from django.db import models

#Create your models here.
#Despues de hacer el modelo debo hacer migrar y hacer migraciones (2 comandos manage.py)
class Contrato(models.Model):
    tipo = models.CharField(max_length=30)
    nombreCliente = models.CharField(max_length=20)
    apellidoCliente = models.CharField(max_length=20)
    fechaCreacion = models.CharField(max_length=20)
    valor = models.IntegerField()

    def __str__(self):
        return self.tipo #Esto me permite ver el tipo en el gestor de django/admin

#Desde hacer las primeras migraciones
#realizo manage.py sqlmigrate *nombreapp* *nombremigracion (0002)* para
#ejecutar la migracion a una tabla sql3
#y ejecuto manage.py migrate para realizarlo.