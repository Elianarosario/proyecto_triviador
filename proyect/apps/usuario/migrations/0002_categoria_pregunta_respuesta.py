# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_cat', models.CharField(max_length=150)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo_pregunta', models.CharField(max_length=150)),
                ('respuesta_1', models.CharField(max_length=200)),
                ('respuesta_2', models.CharField(max_length=200)),
                ('respuesta_3', models.CharField(max_length=200)),
                ('respuesta_correcta', models.CharField(max_length=200)),
                ('nombre_cat', models.ForeignKey(to='usuario.Categoria')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resultado', models.IntegerField(verbose_name=b'0-> incorrecto, 1 -> correcto')),
                ('pregunta', models.ForeignKey(to='usuario.Pregunta')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
