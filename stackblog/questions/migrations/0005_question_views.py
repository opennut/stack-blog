# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_question_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
