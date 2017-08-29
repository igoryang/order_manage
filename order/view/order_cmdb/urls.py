#!/usr/bin/env python
# -*- encoding:utf-8 -*-


from django.conf.urls import include, url
from order.view.order_cmdb  import order_cmdb

urlpatterns = [
    url(r'^$', order_cmdb.ordercmdb),
    url(r'^index$',order_cmdb.ordercmdb),
    url(r'^ordercmdb$', order_cmdb.ordercmdb),
    # url(r'^cluster$', order_cmdb.cluster),
    # url(r'^host$', order_cmdb.host),
    # url(r'^vminstances$', order_cmdb.vminstances),
]
