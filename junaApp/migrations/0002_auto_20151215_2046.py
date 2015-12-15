# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('junaApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asema',
            name='leveys',
            field=models.DecimalField(decimal_places=8, blank=True, max_digits=12),
        ),
        migrations.AlterField(
            model_name='asema',
            name='pituus',
            field=models.DecimalField(decimal_places=8, blank=True, max_digits=12),
        ),
    ]
