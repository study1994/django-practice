# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('choices', '0002_auto_20170516_2047'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'verbose_name': '\u95ee\u7b54\u9898\u578b\u586b\u5199', 'verbose_name_plural': '\u95ee\u7b54\u9898\u578b\u586b\u5199'},
        ),
        migrations.AlterField(
            model_name='content',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 17, 11, 2, 24, 856000), verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='mychoice',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 17, 11, 2, 24, 855000), verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='myquestion',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 17, 11, 2, 24, 855000), verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='mytext',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 17, 11, 2, 24, 856000), verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
