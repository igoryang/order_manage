# -*- encoding:utf-8 -*-

from django.shortcuts import render, HttpResponse
# from app01.lib import zstack_VM_api
# from app01.lib import zstack_PS_api
# from app01.lib import zstack_base_demo
# from app01.lib import zstack_host_api
# from app01.lib import zstack_zone_api
# from app01.lib import zstack_cluster_api
# from app01.models import VmsInfo
import json, chardet
# Create your views here.


def showorder(request):
    return render(request, 'order/showorder.html')

# def lab(request):
#     return render(request, 'order/lab.html')