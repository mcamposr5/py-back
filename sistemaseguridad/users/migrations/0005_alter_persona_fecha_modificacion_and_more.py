# Generated by Django 4.2.16 on 2024-11-07 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_estadocivil_estatuscuenta_persona_tipodocumento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='fecha_modificacion',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='usuario_modificacion',
            field=models.CharField(blank=True, max_length=203, null=True),
        ),
    ]
