# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('junaApp', '0005_auto_20160103_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asema',
            name='leveys',
            field=models.DecimalField(max_digits=12, decimal_places=8),
        ),
        migrations.AlterField(
            model_name='asema',
            name='pituus',
            field=models.DecimalField(max_digits=12, decimal_places=8),
        ),
    ]
