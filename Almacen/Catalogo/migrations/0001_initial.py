# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-11-30 05:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='diametro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primer_diametro', models.CharField(max_length=200)),
                ('ultimo_diametro', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Existencia',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Codigo particular para el tornillos en todo el inventario', primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=500)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('d', 'Disponible'), ('nd', 'No disponible')], default='d', help_text='Disponibilidad del art\xedculo', max_length=1)),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
        migrations.CreateModel(
            name='TipoMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(help_text='Ingrese un tipo de material (e.g Zincado, Bronce, Inox, etc.)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tornillo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=200)),
                ('Tipomaterial', models.ManyToManyField(help_text='Seleccione un tipo de material para este tornillos', to='Catalogo.TipoMaterial')),
            ],
        ),
        migrations.AddField(
            model_name='existencia',
            name='tornillo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Catalogo.Tornillo'),
        ),
    ]