#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from django.conf.urls import include, url
from order.view.show_order import show_order

urlpatterns = [
    url(r'^$', show_order.showorder),
    url(r'^index$', show_order.showorder),
    # url(r'^lab$',  show_order.showorder),
    # url(r'^zone$', product.zone),
    # url(r'^cluster$', product.cluster),
    # url(r'^host$', product.host),
    # url(r'^vminstances$', product.vminstances),

]