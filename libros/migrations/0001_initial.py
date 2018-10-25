# Generated by Django 2.1.1 on 2018-10-25 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre del Libro')),
                ('autor', models.CharField(max_length=200, verbose_name='Autor')),
                ('paginas', models.IntegerField(default=1, verbose_name='Páginas')),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField(default=0, verbose_name='Cantidad de libros')),
                ('libro', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='libros.Libros')),
            ],
        ),
    ]
