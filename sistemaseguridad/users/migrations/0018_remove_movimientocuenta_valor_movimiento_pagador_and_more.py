# Generated by Django 4.2.16 on 2024-11-13 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_alter_tipomovimientocxc_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movimientocuenta',
            name='valor_movimiento_pagador',
        ),
        migrations.AddField(
            model_name='movimientocuenta',
            name='valor_movimiento_pagado',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='movimientocuenta',
            name='valor_movimiento',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='tipomovimientocxc',
            name='operacion_cuenta_corriente',
            field=models.IntegerField(choices=[(1, 'Sumar'), (2, 'Restar')], default=1),
        ),
    ]