# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tags', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now=True, verbose_name=b'Fecha')),
                ('description', markupfield.fields.MarkupField(rendered_field=True, verbose_name=b'Descripcion')),
                ('description_markup_type', models.CharField(default=b'markdown', max_length=30, choices=[(b'', b'--'), (b'markdown', b'markdown')])),
                ('flag', models.BooleanField(default=False)),
                ('_description_rendered', models.TextField(editable=False)),
            ],
            options={
                'verbose_name': 'Respuesta',
                'verbose_name_plural': 'Respuestas',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.SlugField(max_length=200, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'Titulo')),
                ('date', models.DateTimeField(verbose_name=b'Fecha')),
                ('description', markupfield.fields.MarkupField(rendered_field=True, verbose_name=b'Descripcion')),
                ('description_markup_type', models.CharField(default=b'markdown', max_length=30, choices=[(b'', b'--'), (b'markdown', b'markdown')])),
                ('_description_rendered', models.TextField(editable=False)),
                ('views', models.IntegerField(default=0)),
                ('voted', models.IntegerField(default=0)),
                ('estatus', models.BooleanField(default=True)),
                ('tags', models.ManyToManyField(to='tags.Tag')),
                ('user', models.ForeignKey(verbose_name=b'Usuario', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Pregunta',
                'verbose_name_plural': 'Preguntas',
            },
        ),
        migrations.CreateModel(
            name='Vote_Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.ForeignKey(verbose_name=b'Pregunta', to='questions.Question')),
                ('user', models.ForeignKey(verbose_name=b'Usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(verbose_name=b'Pregunta', to='questions.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(verbose_name=b'Usuario', to=settings.AUTH_USER_MODEL),
        ),
    ]
