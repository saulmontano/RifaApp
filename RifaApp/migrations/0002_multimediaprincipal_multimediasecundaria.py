# Generated by Django 5.0 on 2024-04-18 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RifaApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultimediaPrincipal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('imagen_principal', models.ImageField(upload_to='multimedia_principal/')),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MultimediaSecundaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(upload_to='multimedia_secundaria/')),
            ],
        ),
    ]