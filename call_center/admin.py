from django.contrib import admin
from call_center.models import Orden

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ('id_order','empleado','name','DirClient','sucursal','recibido','fecha_recibido','creado')