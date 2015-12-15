# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('junaApp', '0002_auto_20151215_2046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asiakas',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('etunimi', models.CharField(max_length=30)),
                ('sukunimi', models.CharField(max_length=30)),
                ('kotikaupunki', models.CharField(max_length=30)),
                ('salasana', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Varaus',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('varaajan_id', models.IntegerField()),
                ('junan_numero', models.IntegerField()),
                ('varauspaiva', models.DateTimeField()),
                ('lahtoasema', models.CharField(max_length=30)),
                ('maaraasema', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='pysahdys',
            name='asema',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='pysahdys',
            name='junan_numero',
            field=models.IntegerField(),
        ),
    ]
