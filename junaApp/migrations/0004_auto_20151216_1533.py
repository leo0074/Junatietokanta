# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('junaApp', '0003_auto_20151215_2349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='juna',
            old_name='tyyppitunnus',
            new_name='tyyppi',
        ),
    ]
