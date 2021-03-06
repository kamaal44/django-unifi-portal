# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-13 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_unifi_portal', '0003_auto_20170613_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='unifiuser',
            name='about',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='unifiuser',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='unifiuser',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='unifiuser',
            name='language',
            field=models.CharField(default='it-IT', max_length=8),
        ),
        migrations.AddField(
            model_name='unifiuser',
            name='picture',
            field=models.ImageField(default='profile_images/user_no_image.png', null=True, upload_to='profile_images'),
        ),
    ]
