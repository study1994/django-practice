# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionNaire',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30, verbose_name=b'\xe9\x97\xae\xe5\x8d\xb7\xe5\x90\x8d\xe7\xa7\xb0')),
                ('put_time', models.DateTimeField(verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4')),
                ('num', models.IntegerField(default=0, verbose_name=b'\xe9\x97\xae\xe5\x8d\xb7\xe8\xa2\xab\xe5\xa1\xab\xe5\x86\x99\xe6\xac\xa1\xe6\x95\xb0')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u7528\u6237\u4e2a\u4eba\u95ee\u5377',
                'verbose_name_plural': '\u7528\u6237\u4e2a\u4eba\u95ee\u5377',
            },
            bases=(models.Model,),
        ),
    ]
