# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measure', '0002_measure_average'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measure',
            name='average',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
