# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20170904_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciorder',
            name='order_alias',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe7\xb1\xbb\xe5\x9e\x8b', blank=True),
        ),
        migrations.AlterField(
            model_name='ciorder',
            name='order_createdtime',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 4, 20, 7, 12, 754000), verbose_name=b'\xe4\xb8\x8b\xe5\x8d\x95\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='ciorder',
            name='order_delivertime',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 4, 20, 7, 12, 754000), verbose_name=b'\xe4\xba\xa4\xe4\xbb\x98\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='ciproduct',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 4, 20, 7, 12, 755000), verbose_name=b'\xe4\xb8\x8a\xe7\xba\xbf\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='ciproduct',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 4, 20, 7, 12, 755000), verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
