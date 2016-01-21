# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 18:18
from __future__ import unicode_literals

import django.db.models.deletion
import django.views.generic.dates
import sorl.thumbnail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('members', '0001_initial'), ('members', '0002_corporatemember_logo_to_sorlimagefield'), ('members', '0003_allow_null_invoice_sent_date'), ('members', '0004_corporatemember_notes')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CorporateMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=250)),
                ('billing_name', models.CharField(blank=True, help_text='If different from display name.', max_length=250)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='corporate-members')),
                ('description', models.TextField(blank=True)),
                ('url', models.URLField(verbose_name='URL')),
                ('contact_name', models.CharField(max_length=250)),
                ('contact_email', models.EmailField(max_length=254)),
                ('billing_email', models.EmailField(blank=True, help_text='If different from contact email.', max_length=254)),
                ('membership_level', models.IntegerField(choices=[(1, 'Independent consultancy'), (2, 'Small-to-medium business'), (3, 'Large corporation')])),
                ('address', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['display_name'],
            },
        ),
        migrations.CreateModel(
            name='DeveloperMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('member_since', models.DateField(default=django.views.generic.dates.timezone_today)),
                ('member_until', models.DateField(blank=True, null=True)),
                ('reason_for_leaving', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_date', models.DateField(blank=True, null=True)),
                ('amount', models.IntegerField(help_text='In integer dollars')),
                ('paid_date', models.DateField(blank=True, null=True)),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.CorporateMember')),
            ],
        ),
        migrations.AlterField(
            model_name='corporatemember',
            name='logo',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='corporate-members'),
        ),
        migrations.AlterField(
            model_name='corporatemember',
            name='membership_level',
            field=models.IntegerField(choices=[(1, 'Silver'), (2, 'Gold'), (3, 'Platinum')]),
        ),
        migrations.AddField(
            model_name='corporatemember',
            name='notes',
            field=models.TextField(blank=True, help_text='Not displayed publicly.'),
        ),
    ]
