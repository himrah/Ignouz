# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_auto_20170427_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
