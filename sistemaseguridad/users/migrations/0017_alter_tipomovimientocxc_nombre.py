# Generated by Django 4.2.16 on 2024-11-13 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_tipomovimientocxc_operacion_cuenta_corriente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipomovimientocxc',
            name='nombre',
            field=models.CharField(max_length=75),
        ),
    ]