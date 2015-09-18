# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_remove_question_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 17, 8, 2, 21, 736088, tzinfo=utc), verbose_name=b'Fecha', auto_now=True),
            preserve_default=False,
        ),
    ]
