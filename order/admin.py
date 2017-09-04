#!/usr/bin/env python
# -*- encoding:utf-8 -*-
from django.contrib import admin
# Register your models here.
from order import models

# admin.site.register(models.cis,models.ci_type,models.ci_order,models.ci_product)
class ci_tyepAdmin(admin.ModelAdmin):#表ci_type
    list_display = ('type_id','type_name','type_alias','created_time','status') #admin后台添加字段显示
    search_fields = ('type_id','type_name','type_alias')#添加快速查询栏
    list_filter = ('type_id','type_name','type_alias')
    list_per_page = 20  # 设置分页 每页面显示20行

class ci_productAdmin(admin.ModelAdmin):#表ci_product 用Admin的权限添加显示字段和快速查询栏
    list_display = ('product_number','product_type','product_brand','product_model','product_alias'\
                    ,'created_time','update_time','status')  #添加字段显示
    search_fields = ('product_number','product_model')  #添加快速查询栏
    list_filter = ('product_number','product_model') #添加过滤器
    list_per_page = 20 #设置分页 每页面显示20行

class ci_orderAdmin(admin.ModelAdmin):#表ci_order用Admin权限添加显示字段和快速查询栏
    list_display = ('order_number','order_customer','order_type','order_brand','order_model'\
                    ,'order_quantity','order_unitprice','order_owner','order_createdtime'\
                    ,'order_delivertime','update_time','order_complete','order_alias','status')#添加字段显示

    search_fields = ('order_number','order_brand','order_customer','order_type')#添加快速查询栏
    list_filter = ('order_number','order_brand','order_customer','order_type') #添加过滤器
    list_per_page = 20  # 设置分页 每页面显示20行

admin.site.register(models.Cis)
admin.site.register(models.CiType,ci_tyepAdmin)
admin.site.register(models.CiOrder,ci_orderAdmin)
admin.site.register(models.CiProduct,ci_productAdmin)
