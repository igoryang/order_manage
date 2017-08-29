#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from django.conf.urls import include, url
from order.view.product import product

urlpatterns = [
    url(r'^$', product.zone),
    url(r'^index$', product.zone),
    url(r'^zone$', product.zone),
    url(r'^cluster$', product.cluster),
    url(r'^host$', product.host),
    url(r'^vminstances$', product.vminstances),

]