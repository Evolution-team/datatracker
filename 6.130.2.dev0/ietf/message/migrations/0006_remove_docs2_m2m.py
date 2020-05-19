# Copyright The IETF Trust 2019-2020, All Rights Reserved
# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-30 03:32


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0005_copy_docs_m2m_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messagedocs',
            name='document',
        ),
        migrations.RemoveField(
            model_name='messagedocs',
            name='message',
        ),
        migrations.RemoveField(
            model_name='message',
            name='related_docs2',
        ),
        migrations.DeleteModel(
            name='MessageDocs',
        ),
    ]
