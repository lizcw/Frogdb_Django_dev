# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-20 05:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frogs', '0002_auto_20160420_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transporter',
            name='id',
        ),
        migrations.AlterField(
            model_name='transfer',
            name='transporter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transporter', to='frogs.Transporter', verbose_name='Transporter Name'),
        ),
        migrations.AlterField(
            model_name='transporter',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
