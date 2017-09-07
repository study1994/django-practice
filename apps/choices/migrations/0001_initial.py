# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('add_time', models.DateTimeField(default=datetime.datetime(2017, 5, 16, 20, 46, 40, 608000), verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4')),
                ('name', models.TextField(max_length=20, null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe7\xad\x94\xe6\xa1\x88\xe5\x86\x85\xe5\xae\xb9\xe5\xad\x98\xe5\x82\xa8', blank=True)),
            ],
            options={
                'verbose_name': '\u7528\u6237\u95ee\u7b54\u5b58\u50a8',
                'verbose_name_plural': '\u7528\u6237\u95ee\u7b54\u5b58\u50a8',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyChoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('add_time', models.DateTimeField(default=datetime.datetime(2017, 5, 16, 20, 46, 40, 608000), verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4')),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe9\x80\x89\xe9\xa1\xb9')),
                ('num', models.IntegerField(default=0, verbose_name=b'\xe9\x80\x89\xe6\x8b\xa9\xe6\xac\xa1\xe6\x95\xb0')),
            ],
            options={
                'verbose_name': '\u95ee\u9898\u9009\u9879',
                'verbose_name_plural': '\u95ee\u9898\u9009\u9879',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('add_time', models.DateTimeField(default=datetime.datetime(2017, 5, 16, 20, 46, 40, 607000), verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4')),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe9\x97\xae\xe9\xa2\x98\xe5\x90\x8d')),
                ('type', models.CharField(max_length=20, null=True, choices=[(b'1', b'\xe5\x8d\x95\xe9\x80\x89\xe9\xa2\x98'), (b'2', b'\xe5\xa4\x9a\xe9\x80\x89\xe9\xa2\x98'), (b'3', b'\xe5\xa1\xab\xe7\xa9\xba\xe9\xa2\x98')])),
                ('orde', models.IntegerField(default=0, verbose_name=b'\xe9\xa2\x98\xe7\x9b\xae\xe6\x8e\x92\xe5\xba\x8f')),
                ('question', models.ForeignKey(to='users.QuestionNaire')),
            ],
            options={
                'verbose_name': '\u95ee\u9898\u9898\u76ee',
                'verbose_name_plural': '\u95ee\u9898\u9898\u76ee',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyText',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('add_time', models.DateTimeField(default=datetime.datetime(2017, 5, 16, 20, 46, 40, 608000), verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4')),
                ('name', models.TextField(max_length=20, null=True, verbose_name=b'\xe6\x96\x87\xe6\x9c\xac\xe5\x86\x85\xe5\xae\xb9', blank=True)),
                ('question', models.ForeignKey(to='choices.MyQuestion')),
            ],
            options={
                'verbose_name': '\u95ee\u9898\u95ee\u7b54',
                'verbose_name_plural': '\u95ee\u9898\u95ee\u7b54',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='mychoice',
            name='question',
            field=models.ForeignKey(to='choices.MyQuestion'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='content',
            name='mytext',
            field=models.ForeignKey(to='choices.MyText'),
            preserve_default=True,
        ),
    ]
