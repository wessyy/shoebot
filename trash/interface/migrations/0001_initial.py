# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 05:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=500)),
                ('model_name', models.CharField(max_length=500)),
                ('model_number', models.CharField(max_length=10)),
                ('size', models.CharField(max_length=10)),
            ],
        ),
    ]
