# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('choices', '0011_auto_20170621_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ansertime',
            name='anser_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 4, 17, 37, 19, 582000), verbose_name=b'\xe5\x9b\x9e\xe7\xad\x94\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='content',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 4, 17, 37, 19, 581000), verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='mychoice',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 4, 17, 37, 19, 581000), verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='myquestion',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 4, 17, 37, 19, 580000), verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='mytext',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 4, 17, 37, 19, 581000), verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
