# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='image',
            field=models.ImageField(default=b'profile/opennut-default-img.png', upload_to=b'profile/', null=True, verbose_name=b'Foto de Perfil', blank=True),
        ),
    ]
