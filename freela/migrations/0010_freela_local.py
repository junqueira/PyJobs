# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-26 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freela', '0009_auto_20170824_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='freela',
            name='local',
            field=models.CharField(default='', help_text='Preencha com o lugar da vaga, caso seja remota, explicite!', max_length=100, verbose_name='Local da vaga'),
        ),
    ]
