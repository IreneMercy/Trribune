# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-10-02 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_editor_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default=True, upload_to='articles/'),
        ),
    ]
