# -*- encoding:utf-8 -*-
from django.db import models

# Create your models here.
'''
class userinfo(models.Model):
    #如果没有models.AutoField，默认会创建一个id的自增列
    name = models.CharField(max_length=30)
    email = models.EmailField()
    memo = models.TextField()

class User(models.Model):
    username = models.CharField('用户名',max_length=50)
    password = models.CharField('密码',max_length=255)
    email = models.EmailField('邮箱',null=True,blank=True)
    phone = models.CharField('电话',max_length=11,null=True,blank=True)

    group = models.ManyToManyField(UserGroup,verbose_name='用户组')

    create_date = models.DateTimeField('创建时间',auto_now_add=True)
    update_date = models.DateTimeField('最近修改时间',auto_now=True)


'''