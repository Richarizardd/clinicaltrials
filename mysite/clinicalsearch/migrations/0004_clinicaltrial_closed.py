# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinicalsearch', '0003_clinicaltrial_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinicaltrial',
            name='closed',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
