# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinicalsearch', '0002_auto_20160206_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinicaltrial',
            name='url',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
