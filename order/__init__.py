# -*- coding: utf-8 -*-

#####方法一
# from os import path
# from django.apps import AppConfig
# __author__ = 'igroyang'
#
# VERBOSE_APP_NAME = u"订单管理系统"
# def get_current_app_name(file):
#     return path.dirname(file).replace('\\', '/').split('/')[-1]
# class AppVerboseNameConfig(AppConfig):
#     name = get_current_app_name(__file__)
#     verbose_name = VERBOSE_APP_NAME
# default_app_config = get_current_app_name(__file__) + '.__init__.AppVerboseNameConfig'


##########方法2
from django.apps import AppConfig
import os

default_app_config = 'order.PrimaryBlogConfig'

VERBOSE_APP_NAME = u"订单管理"


def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]


class PrimaryBlogConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = VERBOSE_APP_NAME



######方法3 需要在admini.py中设置app中文显示名称
# from django.contrib import admin,auth
#
# admin.default_app_config = 'order.admin.AdminConfig'
# default_app_config = 'order.admin.orderConfig'
# auth.default_app_config = 'order.admin.AuthConfig'
