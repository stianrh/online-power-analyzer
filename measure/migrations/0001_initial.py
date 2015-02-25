# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('voltage', models.FloatField(default=2.8)),
                ('time', models.IntegerField(default=10)),
                ('resolution', models.IntegerField(default=1000)),
                ('measure_list', models.TextField(default=b'None')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
