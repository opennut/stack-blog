# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_question_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='_description_rendered',
            field=models.TextField(default='*test*', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='description_markup_type',
            field=models.CharField(default=None, max_length=30, choices=[(b'', b'--'), (b'html', 'HTML'), (b'plain', 'Plain')]),
        ),
        migrations.AlterField(
            model_name='question',
            name='description',
            field=markupfield.fields.MarkupField(rendered_field=True),
        ),
    ]
