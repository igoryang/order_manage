# -*- encoding:utf-8 -*-


"""
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from app01.lib import zstack_image_api
from app01.lib import zstack_PS_api
from app01.lib import zstack_VM_api
from app01.lib import zstack_base_demo
from app01.lib import zstack_host_api
from app01.lib import zstack_cluster_api
from app01.lib import zstack_zone_api
from app01.lib import zstack_volume_api
from app01.lib import zstack_l3_network
from app01.lib import zstack_report
from app01.lib.cmdb import cmdb_demo

import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# print BASE_DIR
# Create your views here.

def monitor(request):
    return render(request, 'zabbix.html')


def image(request):
    if request.method == "POST":
        base = zstack_base_demo.zstack_base_api()
        page_start = int(request.POST.get('iDisplayStart'))
        page_end = page_start + 20
        new_zs = zstack_image_api.zstack_image_api(base)
        image_list = new_zs.query_all_image()
        data = {
            "iTotalRecords": len(image_list),
            "iTotalDisplayRecords": len(image_list),
            "aaData": image_list[page_start:page_end]
        }
        base.logout(base.UUID)
        return HttpResponse(json.dumps(data))
    return render(request, 'zstack/image.html')


def dashboard(request):
    # base_zstack = zstack_base_demo.zstack_base_api()
    if request.method == "POST":
        base_zstack = zstack_base_demo.zstack_base_api()
        new_zs = zstack_host_api.zstack_host_api(base_zstack)
        c_total, m_total, c_free, m_free = new_zs.query_all_resource()
        new_zs1 = zstack_PS_api.zstack_primarystorage_api(base_zstack)
        disc_total, disc_free, disc_physical_total, disc_physical_free = new_zs1.query_all_resource()
        c_ap = float(c_free) / float(c_total) * 100
        m_ap = float(m_free) / float(m_total) * 100
        d_ap = float(disc_free) / float(disc_total) * 100
        # data = [round(c_ap, 1), round(m_ap, 1), round(d_ap, 1)]
        data = [int(c_ap), int(m_ap), int(d_ap)]

        zs_zone = zstack_zone_api.zstack_zone_api(base_zstack)
        zone_list = zs_zone.query_all_zone()

        zs_cluster = zstack_cluster_api.zstack_cluster_api(base_zstack)
        cluster_list = zs_cluster.query_all_cluster()

        zs_host = zstack_host_api.zstack_host_api(base_zstack)
        host_list = zs_host.query_all_host()

        zs_vms = zstack_VM_api.zstack_vminstance_api(base_zstack)
        vms_list = zs_vms.query_all_vm()

        zs_image = zstack_image_api.zstack_image_api(base_zstack)
        image_list = zs_image.query_all_image()

        zs_volume = zstack_volume_api.zstack_volume_api(base_zstack)
        volume_list = zs_volume.query_all_volume()

        zs_l3network = zstack_l3_network.zstack_l3network_api(base_zstack)
        l3network_list = zs_l3network.query_all_l3network()

        # X轴菜单项
        xAxis = [u"区域", u"集群", u"物理机", u"虚拟机", u"镜像", u"逻辑卷", u"L3网卡"]
        oPtion = [len(zone_list), len(cluster_list), len(host_list), len(vms_list), len(image_list),
                  len(volume_list), len(l3network_list)]
        data.append([xAxis, oPtion])

        # 物理机统计(zb,pbs,jy)
        tongji_data = []
        zones = [u'总部', u'鹏博士', u'世纪互联']
        zb_count = []
        pbs_count = []
        jy_count = []

        # 1 - 数量
        kwargs = {
            "vserver_info": u"zstack"
        }
        server_list = cmdb_demo.query_server_api(**kwargs)
        if server_list is not None and len(server_list) != 0:
            for server in server_list:
                server_id = server.get('_id')
                server_frame = cmdb_demo.query_frame_by_serverid(server_id)
                if len(server_frame) != 0:
                    frame_name = server_frame.get('frame_name')
                    if frame_name.split('_')[0].upper() == "ZB":
                        zb_count.append(server)
                    elif frame_name.split('_')[0].upper() == "PBS":
                        pbs_count.append(server)
                    elif frame_name.split('_')[0].upper() == "JY":
                        jy_count.append(server)

        data_1 = [
            {'value': len(zb_count), 'name': zones[0]},
            {'value': len(pbs_count), 'name': zones[1]},
            {'value': len(jy_count), 'name': zones[2]}
        ]

        # 2 - nettype
        kwargs = {
            # "server_usage": u"数据库",
            "vserver_info": u"zstack",
            "net_type": u"内网",
            # "status": u"在线",
            # "env": u"UAT",
        }
        server_inner = cmdb_demo.query_server_api(**kwargs)
        kwargs = {
            "vserver_info": u"zstack",
            "net_type": u"外网",
        }
        server_outer = cmdb_demo.query_server_api(**kwargs)

        if server_inner is not None and server_outer is not None:
            data_2 = [
                {'value': len(server_inner), 'name': '内网访问'},
                {'value': len(server_outer), 'name': '外网访问'},
            ]
        else:
            data_2 = [
                {'value': 0, 'name': '内网访问'},
                {'value': 0, 'name': '外网访问'},
            ]

        # 3 - APP & DB
        kwargs = {
            "server_usage": u"应用",
            "vserver_info": u"zstack",
        }
        server_app = cmdb_demo.query_server_api(**kwargs)
        kwargs = {
            "server_usage": u"数据库",
            "vserver_info": u"zstack",
            # "net_type": u"内网",
            # "status": u"下线",
            # "env": u"UAT",
        }
        server_db = cmdb_demo.query_server_api(**kwargs)
        if server_app is not None and server_db is not None:
            data_3 = [
                {'value': len(server_app), 'name': '应用'},
                {'value': len(server_db), 'name': '数据库'},
            ]
        else:
            data_3 = [
                {'value': 0, 'name': '应用'},
                {'value': 0, 'name': '数据库'},
            ]

        # 4 - status(在线\待用\维护\下线)
        kwargs = {
            "vserver_info": u"zstack",
            "status": u"在线",
        }
        server_online = cmdb_demo.query_server_api(**kwargs)
        kwargs = {
            "vserver_info": u"zstack",
            "status": u"下线",
        }
        server_offline = cmdb_demo.query_server_api(**kwargs)
        kwargs = {
            "vserver_info": u"zstack",
            "status": u"维护",
        }
        server_maintain = cmdb_demo.query_server_api(**kwargs)
        kwargs = {
            "vserver_info": u"zstack",
            "status": u"待用",
        }
        server_inactive = cmdb_demo.query_server_api(**kwargs)

        data_4 = [
            {'value': len(server_online), 'name': '在线'},
            {'value': len(server_inactive), 'name': '待用'},
            {'value': len(server_maintain), 'name': '维护'},
            {'value': len(server_offline), 'name': '下线'},
        ]

        # 5 - env(生产\测试\UAT\MIT)
        kwargs = {
            "vserver_info": u"zstack",
            "env": u"生产",
        }
        server_prd = cmdb_demo.query_server_api(**kwargs)
        kwargs = {
            "vserver_info": u"zstack",
            "env": u"测试",
        }
        server_sit = cmdb_demo.query_server_api(**kwargs)
        kwargs = {
            "vserver_info": u"zstack",
            "env": u"UAT",
        }
        server_uat = cmdb_demo.query_server_api(**kwargs)
        kwargs = {
            "vserver_info": u"zstack",
            "env": u"MIT",
        }
        server_mit = cmdb_demo.query_server_api(**kwargs)

        data_5 = [
            {'value': len(server_prd), 'name': '生产'},
            {'value': len(server_sit), 'name': '测试'},
            {'value': len(server_uat), 'name': 'UAT'},
            {'value': len(server_mit), 'name': 'MIT'},
        ]

        tongji_data.append(zones)
        tongji_data.append(data_1)
        tongji_data.append(data_2)
        tongji_data.append(data_3)
        tongji_data.append(data_4)
        tongji_data.append(data_5)

        data.append(tongji_data)
        base_zstack.logout(base_zstack.UUID)
        return HttpResponse(json.dumps(data))
    return render(request, 'zstack/dashboard.html')


def resource(request):
    if request.method == "POST":
        page_start = int(request.POST.get('iDisplayStart'))
        page_end = page_start + 20
        page_start = int(request.POST.get('iDisplayStart'))

        data = {
            "iTotalRecords": len(host_list),
            "iTotalDisplayRecords": len(host_list),
            "aaData": host_list[page_start:page_end]
        }
        return JsonResponse(data)
    if request.method == "GET":
        host_list = zstack_report.resource_statistics()
        global host_list
        return render(request, 'zstack/resource.html')


def zabbix(request):
    if request.method == "POST":
        page_start = int(request.POST.get('iDisplayStart'))
        page_end = page_start + 20
        page_start = int(request.POST.get('iDisplayStart'))

        data = {
            "iTotalRecords": len(host_list),
            "iTotalDisplayRecords": len(host_list),
            "aaData": host_list[page_start:page_end]
        }
        return JsonResponse(data)
    if request.method == "GET":
        # host_list = zstack_report.resource_statistics()
        # global host_list
        return render(request, 'zstack/zabbix.html')

"""