# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0013_auto_20170502_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='ans',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
