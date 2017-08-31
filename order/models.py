#!/usr/bin/env python
# -*- encoding:utf-8 -*-
__author__ = 'igoryang'

from django.db import models

# Create your models here.

class cis(models.Model):
    class Meta:
        db_table = 'cis'
    cis_id = models.AutoField(max_length=11,db_column='cis_id',primary_key=True)
    type_id = models.IntegerField(max_length=11,db_column='type_id',blank=False)
    status = models.CharField(max_length=8,db_column='status')
    created_time = models.DateTimeField(auto_now=True)
    heardbeat = models.DateTimeField(auto_now_add=True)


class ci_type(models.Model):
    class Meta:
        db_table = 'ci_type'
    type_id = models.AutoField(max_length=11,db_column='type_id',primary_key=True)
    type_name = models.CharField(max_length=50,db_column='type_name')
    type_alias = models.CharField(max_length=50,db_column='type_alias')
    enabled = models.SmallIntegerField(max_length=11,db_column='enabled')
    is_attached = models.SmallIntegerField(max_length=11,db_column='it_attached',blank=True)
    icon_url = models.CharField(max_length=255,db_column='icon_url')
    order = models.SmallIntegerField(max_length=6,db_column='order')
    created_time = models.DateTimeField(auto_now=True)
    uniq_id = models.IntegerField(max_length=11,db_column='uniq_id')
    status = models.CharField(max_length=8,db_column='status')

class ci_order(models.Model):
    class Meta:
        db_table = 'ci_order'
    order_id = models.AutoField(max_length=11,db_column='order_id',primary_key=True)
    order_number = models.CharField(max_length=255,db_column='order_number')
    order_customer = models.CharField(max_length=50,db_column='order_customer')
    order_type = models.CharField(max_length=50,db_column='order_type')
    order_brand = models.CharField(max_length=50,db_column='order_brand')
    order_quantity = models.IntegerField(max_length=11,db_column='order_quantity')
    order_unitprice = models.IntegerField(max_length=11,db_column='order_unitprice')
    order_owner = models.CharField(max_length=50,db_column='order_owner')
    order_createdtime = models.DateTimeField(auto_now=True)
    order_delivertime = models.DateTimeField(auto_now_add=True)
    order_complete = models.IntegerField(max_length=50,db_column='order_complete')
    order_alias = models.CharField(max_length=50,db_column='order_alias')
    uniq_id = models.IntegerField(max_length=11,db_column='uniq_id')
    status = models.CharField(max_length=8,db_column='status')


class ci_product(models.Model):
    class Meta:
        db_table = 'ci_product'
    product_id = models.AutoField(max_length=11,db_column='product_id',primary_key=True)
    product_number = models.CharField(max_length=255,db_column='product_number')
    product_type = models.CharField(max_length=50,db_column='product_type')
    product_brand = models.CharField(max_length=50,db_column='product_brand')
    product_name = models.CharField(max_length=50,db_column='product_name')
    product_alias = models.CharField(max_length=50,db_column='product_alias')
    created_time = models.DateTimeField(auto_now=True)
    uniq_id = models.IntegerField(max_length=11,db_column='uniq_id')
    status = models.CharField(max_length=8,db_column='stauts')

"""
class ci_customer(models.Model):
    class Meta:
        db_table = 'ci_customer'
    customer_id =
    customer_number =
    customer_name =
    customer_alias =
    customer_company =
    coustomer_address =
    coustomer_phone =
    coustomer_acompany_phone =
    created_time =
    uniq_it =
    status =

class Userinfo(models.Model):
    class Meta:
        db_table = 'userinfo'
    name = models.CharField(max_length=30)
    email = models.EmailField()
    memo = models.TextField()


class Users(models.Model):
    class Meta:
        db_table = 'user'
    id = models.AutoField(max_length=11,db_column='UID',primary_key=True)
    username = models.CharField('用户名',max_length=50)
    nickname = models.CharField('昵称',max_length=50)
    password = models.CharField('密码',max_length=255)
    email = models.EmailField('邮箱',null=True,blank=True)
    mobile = models.CharField('移动电话',max_length=11,null=True,blank=True)
    telephone = models.CharField('电话',max_length=11,null=True,blank=True)
    department = models.CharField('部门',max_length=255)
    user_type = models.CharField('类型',max_length=255)

    group = models.ManyToManyField(UserGroup,verbose_name='用户组')

    create_date = models.DateTimeField('创建时间',auto_now_add=True)
    update_date = models.DateTimeField('最近修改时间',auto_now=True)

class datetimes(models.Model):
    class Meta:
        db_table = 'datetimes'
    value_id = models.AutoField(max_length=11,primary_key=True)
    ci_id = models.IntegerField(max_length=11)
    attr_id = models.IntegerField(max_length=11)
    value = models.DateTimeField(auto_now=True)

"""