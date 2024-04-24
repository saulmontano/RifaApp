# Generated by Django 5.0.4 on 2024-04-21 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RifaApp', '0012_rename_imagenes_imagenesrifa_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='static/img/')),
            ],
            options={
                'verbose_name': 'Imagen',
                'verbose_name_plural': 'Imágenes',
            },
        ),
        migrations.DeleteModel(
            name='ImagenesRifa',
        ),
        migrations.DeleteModel(
            name='ImagenP',
        ),
    ]