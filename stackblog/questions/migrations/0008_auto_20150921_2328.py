# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_auto_20150917_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='description_markup_type',
            field=models.CharField(default=b'markdown', max_length=30, choices=[(b'', b'--'), (b'markdown', b'markdown')]),
        ),
    ]
