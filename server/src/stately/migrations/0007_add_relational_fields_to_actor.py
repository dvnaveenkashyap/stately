# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 22:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stately', '0006_allow_event_actor_to_be_null'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='actions',
            field=models.ManyToManyField(to='stately.Action'),
        ),
        migrations.AddField(
            model_name='actor',
            name='state',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stately.State'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='actor',
            name='case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actors', to='stately.Case'),
        ),
    ]