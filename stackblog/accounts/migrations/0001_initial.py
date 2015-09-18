# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', django_extensions.db.fields.UUIDField(primary_key=True, serialize=False, editable=False, blank=True, verbose_name=b'Id')),
                ('image', models.ImageField(default=None, upload_to=b'profile/', null=True, verbose_name=b'Foto de Perfil', blank=True)),
                ('user', models.OneToOneField(related_name='profile', verbose_name=b'Usuario', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
            },
        ),
    ]
