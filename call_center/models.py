from django.db import models

class Orden(models.Model):
    id_order = models.IntegerField(default=0,null=False,unique=True)
    empleado = models.CharField(max_length=200,null=False)
    cliente = models.TextField()
    descuento = models.IntegerField(default=0)
    impuesto = models.BooleanField(default=False)
    propina = models.BooleanField(default=False)
    valor_extra = models.BooleanField(default=False)
    nit = models.CharField(max_length=200)
    direccion = models.CharField(max_length=500)
    detalles = models.TextField()
    sucursal = models.CharField(max_length=200,null=False)
    recibido = models.BooleanField(default=False)
    fecha_recibido = models.DateTimeField(null=True)
    creado = models.DateTimeField(auto_now_add=True)
