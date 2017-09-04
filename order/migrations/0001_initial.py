# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ci_order',
            fields=[
                ('order_id', models.AutoField(max_length=11, serialize=False, verbose_name=b'ID', primary_key=True)),
                ('order_number', models.CharField(max_length=255, verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe7\xbc\x96\xe7\xa0\x81')),
                ('order_customer', models.CharField(max_length=50, null=True, verbose_name=b'\xe5\xae\xa2\xe6\x88\xb7', blank=True)),
                ('order_type', models.CharField(max_length=5, null=True, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe7\xb1\xbb\xe5\x9e\x8b', blank=True)),
                ('order_brand', models.CharField(max_length=50, null=True, verbose_name=b'\xe5\x93\x81\xe7\x89\x8c', blank=True)),
                ('order_model', models.CharField(max_length=50, null=True, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x9e\x8b\xe5\x8f\xb7', blank=True)),
                ('order_quantity', models.IntegerField(max_length=11, verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe6\x95\xb0\xe9\x87\x8f')),
                ('order_unitprice', models.IntegerField(max_length=1, null=True, verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe5\x8d\x95\xe4\xbb\xb7', blank=True)),
                ('order_owner', models.CharField(max_length=50, null=True, verbose_name=b'\xe4\xb8\x9a\xe5\x8a\xa1\xe5\x91\x98', blank=True)),
                ('order_createdtime', models.DateTimeField(default=-28800, verbose_name=b'\xe4\xb8\x8b\xe5\x8d\x95\xe6\x97\xb6\xe9\x97\xb4')),
                ('order_delivertime', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe4\xba\xa4\xe4\xbb\x98\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('order_complete', models.IntegerField(max_length=50, null=True, verbose_name=b'\xe5\xae\x8c\xe6\x88\x90\xe8\xbf\x9b\xe5\xba\xa6', blank=True)),
                ('order_alias', models.CharField(max_length=50, null=True, verbose_name=b'\xe4\xba\xa7\xe5\x9c\xb0', blank=True)),
                ('uniq_id', models.IntegerField(max_length=11, null=True, blank=True)),
                ('status', models.CharField(max_length=8, null=True, verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe7\x8a\xb6\xe6\x80\x81', blank=True)),
            ],
            options={
                'verbose_name': '\u8ba2\u5355\u7ba1\u7406',
                'verbose_name_plural': '\u8ba2\u5355\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='ci_product',
            fields=[
                ('product_id', models.AutoField(max_length=11, serialize=False, verbose_name=b'ID', primary_key=True)),
                ('product_number', models.CharField(max_length=255, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe7\xbc\x96\xe5\x8f\xb7')),
                ('product_type', models.CharField(max_length=50, null=True, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe7\xb1\xbb\xe5\x9e\x8b', blank=True)),
                ('product_brand', models.CharField(max_length=50, null=True, verbose_name=b'\xe5\x93\x81\xe7\x89\x8c', blank=True)),
                ('product_model', models.CharField(max_length=50, null=True, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe5\x9e\x8b\xe5\x8f\xb7', blank=True)),
                ('product_alias', models.CharField(max_length=50, null=True, verbose_name=b'\xe4\xba\xa7\xe5\x9c\xb0', blank=True)),
                ('created_time', models.DateTimeField(default=-28800, verbose_name=b'\xe4\xb8\x8a\xe7\xba\xbf\xe6\x97\xb6\xe9\x97\xb4')),
                ('update_time', models.DateTimeField(default=-28800, verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
                ('uniq_id', models.IntegerField(max_length=11, null=True, blank=True)),
                ('status', models.CharField(max_length=8, null=True, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81\xe7\x8a\xb6\xe6\x80\x81', blank=True)),
            ],
            options={
                'db_table': 'ci_product',
                'verbose_name': '\u4ea7\u54c1\u7ba1\u7406',
                'verbose_name_plural': '\u4ea7\u54c1\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='ci_type',
            fields=[
                ('type_id', models.AutoField(primary_key=True, db_column=b'type_id', serialize=False, max_length=11, verbose_name='ID')),
                ('type_name', models.CharField(max_length=50, verbose_name='\u7c7b\u578b', db_column=b'type_name')),
                ('type_alias', models.CharField(max_length=50, null=True, db_column=b'type_alias', blank=True)),
                ('icon_url', models.CharField(max_length=255, null=True, db_column=b'icon_url', blank=True)),
                ('order', models.SmallIntegerField(max_length=6, null=True, db_column=b'order', blank=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('uniq_id', models.IntegerField(max_length=11, null=True, db_column=b'uniq_id', blank=True)),
                ('status', models.CharField(max_length=8, null=True, db_column=b'status', blank=True)),
            ],
            options={
                'db_table': 'ci_type',
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='cis',
            fields=[
                ('cis_id', models.AutoField(max_length=11, serialize=False, primary_key=True, db_column=b'cis_id')),
                ('type_id', models.IntegerField(max_length=11, db_column=b'type_id')),
                ('status', models.CharField(max_length=8, null=True, db_column=b'status', blank=True)),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('heardbeat', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'cis',
                'verbose_name': 'CIS',
                'verbose_name_plural': 'CIS',
            },
        ),
    ]
