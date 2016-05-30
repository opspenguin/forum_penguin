# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blocks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u540d\u79f0')),
                ('desc', models.CharField(max_length=200, verbose_name='\u63cf\u8ff0')),
                ('create_timestamp', models.DateField(auto_now_add=True)),
                ('last_update_timestamp', models.DateField(auto_now=True)),
                ('manager', models.ForeignKey(verbose_name=b'\xe7\xae\xa1\xe7\x90\x86\xe5\x91\x98', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
