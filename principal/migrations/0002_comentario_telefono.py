# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-26 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='telefono',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
