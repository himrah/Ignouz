# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import aloha.fields


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0011_auto_20170429_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='ans',
            field=aloha.fields.HTMLField(),
        ),
    ]
