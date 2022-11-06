# Generated by Django 4.1.2 on 2022-11-01 05:24

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
                ('id_order', models.IntegerField(default=0)),
                ('empleado', models.CharField(max_length=200)),
                ('cliente', models.TextField()),
                ('descuento', models.IntegerField(default=0)),
                ('impuesto', models.BooleanField(default=False)),
                ('propina', models.BooleanField(default=False)),
                ('valor_extra', models.BooleanField(default=False)),
                ('nit', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=500)),
                ('detalles', models.TextField()),
                ('sucursal', models.CharField(max_length=200)),
                ('recibido', models.BooleanField(default=False)),
                ('fecha_recibido', models.DateTimeField()),
                ('creado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
