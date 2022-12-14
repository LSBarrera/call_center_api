# Generated by Django 4.1.2 on 2022-11-11 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_order', models.IntegerField(default=0, unique=True)),
                ('name', models.CharField(max_length=250, null=True, verbose_name='Cliente')),
                ('Descuentopociento', models.IntegerField(default=0)),
                ('cobrarimpuesto', models.BooleanField(default=False)),
                ('propina', models.BooleanField(default=False)),
                ('SaldoCliente', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('CobrarValorExtra', models.BooleanField(default=False)),
                ('NombreClientePrepago', models.CharField(max_length=250, null=True)),
                ('CantPersonas', models.IntegerField(default=0)),
                ('DescuentoEspecial', models.BooleanField(default=False)),
                ('DescuentoEn', models.IntegerField(default=0)),
                ('DescuentoLibre', models.BooleanField(default=False)),
                ('DescuentoCortesia', models.BooleanField(default=False)),
                ('ValueNITClient', models.CharField(max_length=255, null=True)),
                ('DirClient', models.CharField(max_length=255, null=True, verbose_name='Dirección')),
                ('TotalSubsidio', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('QuitarSubsidio', models.BooleanField(default=False)),
                ('EsPorCuentaPendiente', models.BooleanField(default=False)),
                ('TipoOrden', models.IntegerField(default=0)),
                ('IDOrdenCE', models.IntegerField(default=0)),
                ('TipoEstadoCE', models.IntegerField(default=0)),
                ('TotalMontoDelivery', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('EsNuevaCE', models.BooleanField(default=False)),
                ('Notas', models.TextField(null=True)),
                ('Payment_ID_CE', models.IntegerField(default=0)),
                ('Delivery_Address_ID_CE', models.IntegerField(default=0)),
                ('Driver_ID_CE', models.IntegerField(default=0)),
                ('Driver_ID_EW', models.IntegerField(default=0)),
                ('Want_FE_CE', models.BooleanField(default=False)),
                ('Document_Type_ID_FE_CE', models.IntegerField(default=0)),
                ('Document_ID_FE_CE', models.CharField(max_length=100, null=True)),
                ('Email_Client_FE_CE', models.CharField(max_length=150, null=True)),
                ('Email_Client_CE', models.CharField(max_length=150, null=True)),
                ('Telefono_Client_CE', models.CharField(max_length=50, null=True)),
                ('Nombre_Mesa_CE', models.CharField(max_length=150, null=True)),
                ('Mesa_ID_CE', models.IntegerField(default=0)),
                ('MetodoPago_CE', models.CharField(max_length=100, null=True)),
                ('TipoConsumoCE', models.IntegerField(default=0)),
                ('CobrarDeliveryCE', models.BooleanField(default=False)),
                ('Eliminada_CE', models.BooleanField(default=False)),
                ('Eliminada_Aplicada_CE', models.BooleanField(default=False)),
                ('orden_impresa', models.BooleanField(default=False)),
                ('CuponWeb', models.CharField(max_length=100, null=True)),
                ('retencion', models.BooleanField(default=False)),
                ('TypeCoupon', models.CharField(max_length=50, null=True)),
                ('Coupons_Real_Value', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('Coupons_Perceived_Value', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('Client_IntegrationCode', models.CharField(max_length=100, null=True)),
                ('TotalRedemptionsAvailablePerCoupon', models.IntegerField(default=0)),
                ('TotalRedemptionsAvailablePerUser', models.IntegerField(default=0)),
                ('cliente', models.TextField(null=True)),
                ('empleado', models.CharField(max_length=200)),
                ('telefono_cliente', models.CharField(max_length=100)),
                ('detalles', models.TextField(null=True)),
                ('nota', models.TextField(null=True)),
                ('sucursal', models.CharField(max_length=200)),
                ('recibido', models.BooleanField(default=False)),
                ('fecha_recibido', models.DateTimeField(null=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
