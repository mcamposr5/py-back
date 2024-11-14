# Generated by Django 4.2.16 on 2024-11-13 23:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_alter_saldocuenta_creditos_alter_saldocuenta_debitos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='opcion',
            name='pagina',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='movimientocuenta',
            name='fecha_movimiento',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 13, 23, 11, 55, 490549, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='movimientocuenta',
            name='generado_automaticamente',
            field=models.BooleanField(choices=[(True, 'Si'), (False, 'No')], default=False),
        ),
        migrations.AlterField(
            model_name='tipomovimientocxc',
            name='operacion_cuenta_corriente',
            field=models.IntegerField(choices=[(1, 'Sumar'), (2, 'Restar')], default=1),
        ),
    ]
