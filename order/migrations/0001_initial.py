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
                ('order_id', models.AutoField(max_length=11, serialize=False, primary_key=True, db_column=b'order_id')),
                ('order_number', models.CharField(max_length=255, db_column=b'order_number')),
                ('order_customer', models.CharField(max_length=50, db_column=b'order_customer')),
                ('order_type', models.CharField(max_length=50, db_column=b'order_type')),
                ('order_brand', models.CharField(max_length=50, db_column=b'order_brand')),
                ('order_quantity', models.IntegerField(max_length=11, db_column=b'order_quantity')),
                ('order_unitprice', models.IntegerField(max_length=11, db_column=b'order_unitprice')),
                ('order_owner', models.CharField(max_length=50, db_column=b'order_owner')),
                ('order_createdtime', models.DateTimeField(auto_now=True)),
                ('order_delivertime', models.DateTimeField(auto_now_add=True)),
                ('order_complete', models.IntegerField(max_length=50, db_column=b'order_complete')),
                ('order_alias', models.CharField(max_length=50, db_column=b'order_alias')),
                ('uniq_id', models.IntegerField(max_length=11, db_column=b'uniq_id')),
                ('status', models.CharField(max_length=8, db_column=b'status')),
            ],
            options={
                'db_table': 'ci_order',
            },
        ),
        migrations.CreateModel(
            name='ci_product',
            fields=[
                ('product_id', models.AutoField(max_length=11, serialize=False, primary_key=True, db_column=b'product_id')),
                ('product_number', models.CharField(max_length=255, db_column=b'product_number')),
                ('product_type', models.CharField(max_length=50, db_column=b'product_type')),
                ('product_brand', models.CharField(max_length=50, db_column=b'product_brand')),
                ('product_name', models.CharField(max_length=50, db_column=b'product_name')),
                ('product_alias', models.CharField(max_length=50, db_column=b'product_alias')),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('uniq_id', models.IntegerField(max_length=11, db_column=b'uniq_id')),
                ('status', models.CharField(max_length=8, db_column=b'stauts')),
            ],
            options={
                'db_table': 'ci_product',
            },
        ),
        migrations.CreateModel(
            name='ci_type',
            fields=[
                ('type_id', models.AutoField(max_length=11, serialize=False, primary_key=True, db_column=b'type_id')),
                ('type_name', models.CharField(max_length=50, db_column=b'type_name')),
                ('type_alias', models.CharField(max_length=50, db_column=b'type_alias')),
                ('enabled', models.SmallIntegerField(max_length=11, db_column=b'enabled')),
                ('is_attached', models.SmallIntegerField(max_length=11, db_column=b'it_attached', blank=True)),
                ('icon_url', models.CharField(max_length=255, db_column=b'icon_url')),
                ('order', models.SmallIntegerField(max_length=6, db_column=b'order')),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('uniq_id', models.IntegerField(max_length=11, db_column=b'uniq_id')),
                ('status', models.CharField(max_length=8, db_column=b'status')),
            ],
            options={
                'db_table': 'ci_type',
            },
        ),
        migrations.CreateModel(
            name='cis',
            fields=[
                ('cis_id', models.AutoField(primary_key=True, db_column=b'cis_id', serialize=False, max_length=11, verbose_name='')),
                ('type_id', models.IntegerField(max_length=11, db_column=b'type_id')),
                ('status', models.CharField(max_length=8, db_column=b'status')),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('heardbeat', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'cis',
            },
        ),
    ]
