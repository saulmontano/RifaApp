# Generated by Django 5.0.4 on 2024-04-21 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RifaApp', '0015_rifa_rango_numeros_rifa_valor_por_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rifa',
            name='valor_por_numero',
            field=models.CharField(max_length=20),
        ),
    ]