# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-21 00:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stately', '0016_make_case_id_field_uuid'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActorAuthenticator',
            fields=[
                ('token', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('generated_at', models.DateTimeField(auto_now_add=True)),
                ('is_valid', models.BooleanField(default=True)),
                ('actor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auths', to='stately.Actor')),
            ],
        ),
    ]
