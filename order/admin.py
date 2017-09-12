#!/usr/bin/env python
# -*- encoding:utf-8 -*-
from django.contrib import admin
# Register your models here.
from order import models
from django.contrib import admin
# from django.contrib.auth.apps import AuthConfig as _AuthConfig
# from django.contrib.admin.apps import AdminConfig as _AdminConfig
# from django.apps import AppConfig
#
# #方法3
# class orderConfig(AppConfig):
#     name = u'order'
#     verbose_name = u"订单管理"


# class AuthConfig(_AuthConfig):
#     name = 'django.contrib.auth'
#     verbose_name = u'用户管理'
#
#
# class AdminConfig(_AdminConfig):
#     name = 'django.contrib.admin'
#     verbose_name = u'后台管理'


# admin.site.register(models.cis,models.ci_type,models.ci_order,models.ci_product)

class ci_tyepAdmin(admin.ModelAdmin):  # 表ci_type
    list_display = ('type_id', 'type_name', 'type_alias', 'created_time', 'status')  # admin后台添加字段显示
    search_fields = ('type_id', 'type_name', 'type_alias')  # 添加快速查询栏
    list_filter = ('type_id', 'type_name', 'type_alias')
    list_per_page = 20  # 设置分页 每页面显示20行
    list_editable = ['status']  # 设置默认可编辑字段
    # fk_fields =('','')设置显示外键字段
    # fields=('type_name','type_alias','status') #防止重要字段被修改，在fields中不要列出即可
    # filter_horizontal = ('type_name','type_alias' ) 管理页面编辑菜单自定义多对多字段
    # raw_id_fields = ('','' )管理页面编辑菜单自定义外键的修改


class ci_productAdmin(admin.ModelAdmin):  # 表ci_product 用Admin的权限添加显示字段和快速查询栏
    list_display = ('product_number', 'product_type', 'product_brand', 'product_model', 'product_alias' \
                        , 'created_time', 'update_time', 'status')  # 添加字段显示
    search_fields = ('product_number', 'product_model')  # 添加快速查询栏
    list_filter = ('product_number', 'product_model')  # 添加过滤器
    list_per_page = 20  # 设置分页 每页面显示20行
    list_editable = ['status']  # 设置默认可编辑字段
    actions_on_top = True  # 顶部显示的属性，设置为True在顶部显示，设置为False不在顶部显示，默认为True。
    actions_on_bottom = False  # 底部显示的属性，设置为True在底部显示，设置为False不在底部显示，默认为False。
    # fk_fields =('','')设置显示外键字段
    date_hierarchy = 'created_time'  # 详细时间分层筛选
    # list_display_links = ('product_type') #设置哪些字段可以点击进入编辑界面 必是列表
    # ordering = ('-publish_time')  # ordering设置默认排序字段，负号表示降序排序   models里字段也可以排序


# @admin.register(models.CiOrder)
class ci_orderAdmin(admin.ModelAdmin):  # 表ci_order用Admin权限添加显示字段和快速查询栏
    list_display = ('order_number', 'order_customer', 'order_type', 'order_brand', 'order_model' \
                        , 'order_quantity', 'order_unitprice', 'order_owner', 'order_createdtime' \
                        , 'order_delivertime', 'update_time', 'order_complete', 'order_alias', 'status')  # 添加字段显示

    search_fields = ('order_number', 'order_brand', 'order_customer', 'order_type')  # 添加快速查询栏
    list_filter = ('order_number', 'order_brand', 'order_customer', 'order_type')  # 添加过滤器
    list_per_page = 20  # 设置分页 每页面显示20行
    list_editable = ['status']  # 设置默认可编辑字段
    # fk_fields =('','')设置显示外键字段
    # fieldsets = (  # # 分组表单
    #     ('基本信息', {'fields': ('title', 'content', 'excerpt', 'publish_date','status', 'user', 'categories')}),
    #     ('Meta Data', {'fields': ('alias', 'keywords', 'description')}),
    # )


# # # #调整页面头部显示内容和页面标题

admin.site.site_header = "订单资源管理系统"
admin.site.site_title = "订单管理"

# 注册到admin.site.register
admin.site.register(models.Cis)
admin.site.register(models.CiType, ci_tyepAdmin)
admin.site.register(models.CiOrder, ci_orderAdmin)
admin.site.register(models.CiProduct, ci_productAdmin)











# 通过当前登录的用户过滤显示的数据 官方文档的介绍：
#
# 实际代码和效果：
#
# @admin.register(MachineInfo)
# class MachineInfoAdmin(admin.ModelAdmin):
#     def get_queryset(self, request):
#         """函数作用：使当前登录的用户只能看到自己负责的服务器"""
#         qs = super(MachineInfoAdmin, self).get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(user=UserInfo.objects.filter(user_name=request.user))
#
#     list_display = ('machine_ip', 'application', 'colored_status', 'user', 'machine_model', 'cache',
#                     'cpu', 'hard_disk', 'machine_os', 'idc', 'machine_group')
