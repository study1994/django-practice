# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('choices', '0007_auto_20170609_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 9, 11, 4, 36, 702000), verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='mychoice',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 9, 11, 4, 36, 702000), verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='myquestion',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 9, 11, 4, 36, 701000), verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='mytext',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 9, 11, 4, 36, 702000), verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
