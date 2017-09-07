# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_emailverifyrecord'),
        ('choices', '0010_auto_20170609_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnserTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anser_time', models.DateTimeField(default=datetime.datetime(2017, 6, 21, 16, 22, 6, 127000), verbose_name=b'\xe5\x9b\x9e\xe7\xad\x94\xe6\x97\xb6\xe9\x97\xb4')),
                ('question', models.ForeignKey(to='users.QuestionNaire')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u95ee\u5377\u586b\u5199\u65f6\u95f4',
                'verbose_name_plural': '\u7528\u6237\u95ee\u5377\u586b\u5199\u65f6\u95f4',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='content',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 21, 16, 22, 6, 126000), verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='mychoice',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 21, 16, 22, 6, 126000), verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='myquestion',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 21, 16, 22, 6, 125000), verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='mytext',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 21, 16, 22, 6, 126000), verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
