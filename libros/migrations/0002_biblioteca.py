# Generated by Django 2.1.1 on 2018-10-25 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biblioteca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre de la biblioteca')),
                ('direccion', models.CharField(max_length=200, verbose_name='Dirección')),
            ],
        ),
    ]
