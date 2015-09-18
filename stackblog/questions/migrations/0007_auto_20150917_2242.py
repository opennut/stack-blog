# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20150917_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='description',
            field=markupfield.fields.MarkupField(rendered_field=True, verbose_name=b'Descripcion'),
        ),
    ]
