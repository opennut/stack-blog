# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0009_auto_20150921_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='id',
            field=models.SlugField(default=1, max_length=200, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=100, verbose_name=b'Titulo'),
        ),
    ]
