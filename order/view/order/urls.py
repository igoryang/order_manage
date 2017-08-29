#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from django.conf.urls import include, url
from order.view.order import order

urlpatterns = [
    url(r'^$', order.zone),
    url(r'^index$', order.zone),
    url(r'^zone$', order.zone),
    url(r'^cluster$', order.cluster),
    url(r'^host$', order.host),
    url(r'^vminstances$', order.vminstances),

]