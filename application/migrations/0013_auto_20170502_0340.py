# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0012_auto_20170502_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='ans',
            field=models.TextField(),
        ),
    ]
