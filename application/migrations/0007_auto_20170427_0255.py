# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_qoa_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='QandA',
        ),
        migrations.AlterField(
            model_name='qoa',
            name='code',
            field=models.ForeignKey(to='application.Subject'),
        ),
    ]
