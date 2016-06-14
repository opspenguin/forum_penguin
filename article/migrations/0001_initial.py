# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('block', '0002_auto_20160530_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30, verbose_name='\u6807\u9898')),
                ('content', models.CharField(max_length=10000, verbose_name='\u5185\u5bb9')),
                ('status', models.CharField(default=0, max_length=10, verbose_name='\u72b6\u6001', choices=[(0, '\u666e\u901a'), (-1, '\u5220\u9664'), (10, b'\xe7\xb2\xbe\xe5\x8d\x8e')])),
                ('create_timestamp', models.DateField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('last_update_timestamp', models.DateField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('block', models.ForeignKey(verbose_name='\u677f\u5757', to='block.Blocks')),
                ('owner', models.ForeignKey(verbose_name='\u4f5c\u8005', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
    ]
