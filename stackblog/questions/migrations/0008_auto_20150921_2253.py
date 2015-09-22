# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0007_auto_20150917_2242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now=True, verbose_name=b'Fecha')),
                ('description', markupfield.fields.MarkupField(rendered_field=True, verbose_name=b'Descripcion')),
                ('description_markup_type', models.CharField(default=b'markdown', max_length=30, choices=[(b'', b'--'), (b'markdown', b'markdown')])),
                ('flag', models.BooleanField(default=True)),
                ('_description_rendered', models.TextField(editable=False)),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answer',
            },
        ),
        migrations.AlterField(
            model_name='question',
            name='description_markup_type',
            field=models.CharField(default=b'markdown', max_length=30, choices=[(b'', b'--'), (b'markdown', b'markdown')]),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(verbose_name=b'Question', to='questions.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(verbose_name=b'Usuario', to=settings.AUTH_USER_MODEL),
        ),
    ]
