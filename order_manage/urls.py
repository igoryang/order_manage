"""order_manage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin
from order import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^dashboard/', include("order_cmdb.view.dashboard.urls")),
    url(r'^order_cmdb/', include("order.view.order_cmdb.urls")),
    url(r'^product/', include("order.view.product.urls")),
    url(r'^show_order/', include("order.view.show_order.urls")),
    # url(r'^time/$', include("admin.site.urls")),
    # url(r'^task', include("order_cmdb.view.task.urls")),
]

