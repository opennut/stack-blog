# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now=True, verbose_name=b'Fecha')),
                ('title', models.CharField(max_length=100, verbose_name=b'Titulo')),
                ('description', models.TextField(verbose_name=b'Descripcion')),
                ('estatus', models.BooleanField(default=True)),
                ('tags', models.ManyToManyField(to='tags.Tag')),
                ('user', models.ForeignKey(verbose_name=b'Usuario', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
    ]
