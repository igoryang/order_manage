#!/usr/bin/env python
# -*- encoding:utf-8 -*-
from time import timezone
import django.utils.timezone as timezone
import datetime
from pytz import utc

__author__ = 'igoryang'

from django.contrib import admin
from django.utils.text import capfirst
from django.utils.datastructures import SortedDict


def find_model_index(name):
    count = 0
    for model, model_admin in admin.site._registry.items():
        if capfirst(model._meta.verbose_name_plural) == name:
            return count
        else:
            count += 1
    return count


def index_decorator(func):
    def inner(*args, **kwargs):
        templateresponse = func(*args, **kwargs)
        for app in templateresponse.context_data['app_list']:
            app['models'].sort(key=lambda x: find_model_index(x['name']))
        return templateresponse

    return inner


registry = SortedDict()
registry.update(admin.site._registry)
admin.site._registry = registry
admin.site.index = index_decorator(admin.site.index)
admin.site.app_index = index_decorator(admin.site.app_index)


from django.db import models

# Create your models here.

class cis(models.Model):
    class Meta:
        db_table = 'cis'
        verbose_name = verbose_name_plural = 'CIS'  # 表名称 别名 中文显示
    cis_id = models.AutoField(max_length=11,db_column='cis_id',primary_key=True)
    type_id = models.IntegerField(max_length=11,db_column='type_id',blank=False)
    status = models.CharField(max_length=8,db_column='status',null=True,blank=True)
    created_time = models.DateTimeField(auto_now=True)
    # update_time = models.DateTimeField(default=datetime.now().replace(tzinfo=utc))
    heardbeat = models.DateTimeField(auto_now_add=True)

#写法1  ci_type创建表名称， type_id创建字段名称  db_colunm=''创建列表名称 verbose_name=u""列表字段别名中文显示
class ci_type(models.Model):
    class Meta:
        db_table = 'ci_type'  #创建表名称
        verbose_name = '分类'  #表名称 别名 中文显示
        verbose_name_plural = '分类'  #表名称 别名 中文显示
        # ordering = ['sort']
    type_id = models.AutoField(max_length=11,db_column='type_id',primary_key=True,verbose_name=u'ID') #db_column 创建列字段
    type_name = models.CharField(max_length=50,db_column='type_name',verbose_name=u"类型") #verbose_name字段中文显示
    type_alias = models.CharField(max_length=50,db_column='type_alias',null=True,blank=True)
    icon_url = models.CharField(max_length=255,db_column='icon_url',null=True,blank=True) #blank 可以为空；填充null
    order = models.SmallIntegerField(max_length=6,db_column='order',null=True,blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    uniq_id = models.IntegerField(max_length=11,db_column='uniq_id',null=True,blank=True)
    status = models.CharField(max_length=8,db_column='status',null=True,blank=True)

#写法2  ci_order默认类为表名称；order_id默认为列表字段
class ci_order(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = '订单管理'  #表名称 别名 中文显示
    order_id = models.AutoField('ID',max_length=11,primary_key=True)
    order_number = models.CharField('订单编码',max_length=255)
    order_customer = models.CharField('客户',max_length=50,null=True,blank=True)
    order_type = models.CharField('产品类型',max_length=5,null=True,blank=True)
    order_brand = models.CharField('品牌',max_length=50,null=True,blank=True)
    order_model = models.CharField('产品型号',max_length=50,null=True,blank=True)
    order_quantity = models.IntegerField('订单数量',max_length=11)
    order_unitprice = models.IntegerField('订单单价',max_length=1,null=True,blank=True)
    order_owner = models.CharField('业务员',max_length=50,null=True,blank=True)
    order_createdtime = models.DateTimeField('下单时间',default=timezone.now())
    order_delivertime = models.DateTimeField('交付时间',default=timezone.now())
    update_time = models.DateTimeField('更新时间',auto_now=True)
    order_complete = models.IntegerField('完成进度',max_length=50,null=True,blank=True)
    order_alias = models.CharField('产地',max_length=50,null=True,blank=True)
    uniq_id = models.IntegerField(max_length=11,null=True,blank=True)
    status = models.CharField('订单状态',max_length=8,null=True,blank=True)


class ci_product(models.Model):
    class Meta:
        db_table = 'ci_product'
        verbose_name = '产品管理'  # 表名称 别名 中文显示
        verbose_name_plural = '产品管理'  # 表名称 别名 中文显示
    product_id = models.AutoField('ID',max_length=11,primary_key=True)
    product_number = models.CharField('产品编号',max_length=255)
    product_type = models.CharField('产品类型',max_length=50,null=True,blank=True)
    product_brand = models.CharField('品牌',max_length=50,null=True,blank=True)
    product_model = models.CharField('产品型号',max_length=50,null=True,blank=True)
    product_alias = models.CharField('产地',max_length=50,null=True,blank=True)
    created_time = models.DateTimeField('上线时间',default=timezone.now())
    update_time = models.DateTimeField('更新时间',default=timezone.now())
    uniq_id = models.IntegerField(max_length=11,null=True,blank=True)
    status = models.CharField('产品状态',max_length=8,null=True,blank=True)

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