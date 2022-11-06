from django.contrib import admin
from call_center.models import Orden

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ('id_order','empleado','descuento','impuesto','propina','valor_extra','nit','direccion','sucursal','recibido','fecha_recibido','creado')