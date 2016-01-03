# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('junaApp', '0004_auto_20151216_1533'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pysahdys',
            old_name='junan_numero',
            new_name='junannumero',
        ),
    ]
