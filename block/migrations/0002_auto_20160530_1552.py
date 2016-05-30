# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blocks',
            options={'verbose_name': '\u677f\u5757', 'verbose_name_plural': '\u677f\u5757'},
        ),
        migrations.AlterField(
            model_name='blocks',
            name='create_timestamp',
            field=models.DateField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='blocks',
            name='last_update_timestamp',
            field=models.DateField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4'),
        ),
    ]
