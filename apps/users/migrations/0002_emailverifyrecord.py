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
            name='EmailVerifyRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=20, verbose_name=b'\xe9\xaa\x8c\xe8\xaf\x81\xe7\xa0\x81')),
                ('email', models.EmailField(max_length=50, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1')),
                ('send_type', models.CharField(max_length=18, verbose_name=b'\xe9\xaa\x8c\xe8\xaf\x81\xe7\xa0\x81\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(b'register', b'\xe9\x82\xae\xe7\xae\xb1'), (b'forget', b'\xe4\xbf\xae\xe6\x94\xb9\xe5\xaf\x86\xe7\xa0\x81'), (b'update_email', b'\xe4\xbf\xae\xe6\x94\xb9\xe9\x82\xae\xe7\xae\xb1')])),
                ('send_time', models.DateField(default=datetime.datetime.now, verbose_name=b'\xe5\x8f\x91\xe9\x80\x81\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'verbose_name': '\u90ae\u7bb1\u9a8c\u8bc1\u7801',
                'verbose_name_plural': '\u90ae\u7bb1\u9a8c\u8bc1\u7801',
            },
            bases=(models.Model,),
        ),
    ]
