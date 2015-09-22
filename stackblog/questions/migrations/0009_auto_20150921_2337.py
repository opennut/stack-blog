# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_auto_20150921_2328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='id',
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=100, serialize=False, verbose_name=b'Titulo', primary_key=True),
        ),
    ]
