# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0010_qoa_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='marks',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='subject',
            name='time',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
