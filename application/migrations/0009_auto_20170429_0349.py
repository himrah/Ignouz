# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0008_auto_20170427_0256'),
    ]

    operations = [
        migrations.AddField(
            model_name='qoa',
            name='q_no',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='qoa',
            name='sub_q',
            field=models.CharField(max_length=3, blank=True),
        ),
    ]
