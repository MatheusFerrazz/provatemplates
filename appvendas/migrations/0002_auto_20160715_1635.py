# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appvendas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='matricula',
            field=models.CharField(max_length=10, unique=True, verbose_name='Matrícula'),
        ),
    ]
