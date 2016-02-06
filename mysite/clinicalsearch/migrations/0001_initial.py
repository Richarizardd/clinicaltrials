# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicalTrail',
            fields=[
                ('id', models.TextField(serialize=False, primary_key=True)),
                ('sponsor', models.TextField()),
                ('published', models.BooleanField()),
                ('state', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
