# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 07:11
from __future__ import unicode_literals

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('releases', '0001_initial'), ('releases', '0002_release_eol_date'), ('releases', '0003_populate_release_eol_date'), ('releases', '0004_make_release_date_nullable')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Release',
            fields=[
                ('version', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, default=datetime.date.today, help_text="Leave blank if the release date isn't know yet, typically if you're creating the final release just after the alpha because you want to build docs for the upcoming version.", null=True, verbose_name='Release date')),
                ('major', models.PositiveSmallIntegerField(editable=False)),
                ('minor', models.PositiveSmallIntegerField(editable=False)),
                ('micro', models.PositiveSmallIntegerField(editable=False)),
                ('status', models.CharField(choices=[('a', 'alpha'), ('b', 'beta'), ('c', 'release candidate'), ('f', 'final')], editable=False, max_length=1)),
                ('iteration', models.PositiveSmallIntegerField(editable=False)),
                ('is_lts', models.BooleanField(default=False, verbose_name='Long term support release')),
                ('eol_date', models.DateField(blank=True, help_text="Leave blank if the end of life date isn't known yet, typically because it depends on the release date of a later version.", null=True, verbose_name='End of life date')),
            ],
        ),
    ]
