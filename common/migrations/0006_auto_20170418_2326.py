# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-18 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20150718_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content_markup_type',
            field=models.CharField(choices=[(b'', b'--'), (b'html', 'HTML'), (b'plain', 'Plain'), (b'markdown', 'Markdown'), (b'restructuredtext', 'Restructured Text')], default=b'restructuredtext', editable=False, max_length=30),
        ),
    ]
