# -*- encoding:utf-8 -*-
"""
Django settings for order_manage project.

Generated by 'django-admin startproject' using Django 1.8.14.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e2y81t7vw2^ye-1ziwxch+mctr-)#(-dv@db1g7%bx$b&3ytqs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition  #app 排列顺序

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'order',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.locale.LocaleMiddleware',  #设置显示中文
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'order_manage.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'order_manage.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'order',
        'USER': 'root',
        'PASSWORD': '123.abc',
        'HOST': 'localhost',
        'PORT': '3306',

    }
}
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

# LANGUAGE_CODE = 'en-us'
#
# TIME_ZONE = 'UTC'

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'
# #admin界面汉化#默认admin后台管理界面是英文的，对英语盲来说用起来不方便。可以在settings.py中设置：
# 1.8以前版本
# LANGUAGE_CODE = 'zh-CN'
# TIME_ZONE = 'Asia/Shanghai'
# 1.8版本之后的language code设置不同：
# LANGUAGE_CODE = 'zh-hans'
# TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False
# USE_TZ = True

# LIST_PER_PAGE = 20
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# 设置图片保存路径
MEDIA_URL = '/upload/'
MEDIA_ROOT = os.path.join(BASE_DIR, "static/upload")


# Django  admin 使用suit 小记  suit.官网 http://djangosuit.com/
# SUIT_CONFIG = {  # suit页面配置
#     'ADMIN_NAME': '密码管理系统',  # 登录界面提示
#     'LIST_PER_PAGE': 10,  # 分页,每页显示10条记录
#     'MENU': (
#         # 每一个字典表示左侧菜单的一栏
#         {'label': '密码管理', 'app': 'app01', 'models': ('app01.PwdInfo',)},
#              ),
#     # label表示name，app表示上边的install的app，models表示用了哪些models
# }
