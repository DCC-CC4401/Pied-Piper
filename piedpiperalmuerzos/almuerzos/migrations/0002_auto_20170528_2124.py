# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 01:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('almuerzos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='userType',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='almuerzos.UserType'),
        ),
    ]
