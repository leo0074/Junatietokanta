# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asema',
            fields=[
                ('nimi', models.CharField(primary_key=True, serialize=False, max_length=30)),
                ('kaupunki', models.CharField(max_length=30)),
                ('pituus', models.DecimalField(decimal_places=10, max_digits=10, blank=True)),
                ('leveys', models.DecimalField(decimal_places=10, max_digits=10, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Juna',
            fields=[
                ('numero', models.IntegerField(primary_key=True, serialize=False)),
                ('tyyppitunnus', models.CharField(max_length=5)),
                ('lahtoasema', models.CharField(max_length=30)),
                ('lahtoaika', models.TimeField()),
                ('paateasema', models.CharField(max_length=30)),
                ('saapumisaika', models.TimeField()),
                ('kulkupaivat', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Pysahdys',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('saapumisaika', models.TimeField()),
                ('lahtoaika', models.TimeField()),
                ('asema', models.ForeignKey(to='junaApp.Asema')),
                ('junan_numero', models.ForeignKey(to='junaApp.Juna')),
            ],
        ),
    ]
