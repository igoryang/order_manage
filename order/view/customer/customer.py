# -*- encoding:utf-8 -*-

from django.shortcuts import render, HttpResponse

# from app01.lib import zstack_VM_api
# from app01.lib import zstack_PS_api
# from app01.lib import zstack_base_demo
# from app01.lib import zstack_host_api
# from app01.lib import zstack_zone_api
# from app01.lib import zstack_cluster_api
# from app01.models import VmsInfo
# import json, chardet
# Create your views here.


"""
def zone(request):
    base = zstack_base_demo.zstack_base_api()
    if request.method == "POST":
        page_start = int(request.POST.get('iDisplayStart'))
        page_end = page_start + 20
        # name = request.POST.get('name')
        new_zs = zstack_zone_api.zstack_zone_api(base)
        zone_list = new_zs.query_all_zone()
        data = {
            "iTotalRecords": len(zone_list),
            "iTotalDisplayRecords": len(zone_list),
            "aaData": zone_list[page_start:page_end]
        }
        # json_data = serializers.serialize("json", data)
        new_zs.logout(new_zs.UUID)
        return HttpResponse(json.dumps(data))

    return render(request, 'order/zone.html')

def cluster(request):
    base = zstack_base_demo.zstack_base_api()
    if request.method == "POST":
        page_start = int(request.POST.get('iDisplayStart'))
        page_end = page_start + 20
        new_zs = zstack_cluster_api.zstack_cluster_api(base)
        cluster_list = new_zs.query_all_cluster()
        data = {
            "iTotalRecords": len(cluster_list),
            "iTotalDisplayRecords": len(cluster_list),
            "aaData": cluster_list[page_start:page_end]
        }
        new_zs.logout(new_zs.UUID)
        return HttpResponse(json.dumps(data))

    return render(request, 'order/cluster.html')


def host(request):
    if request.method == "POST":
        base = zstack_base_demo.zstack_base_api()
        page_start = int(request.POST.get('iDisplayStart'))
        page_end = page_start + 20
        new_zs = zstack_host_api.zstack_host_api(base)
        host_list = new_zs.query_all_host()
        data = {
            "iTotalRecords": len(host_list),
            "iTotalDisplayRecords": len(host_list),
            "aaData": host_list[page_start:page_end]
        }
        new_zs.logout(new_zs.UUID)
        return HttpResponse(json.dumps(data))
    return render(request, 'order/host.html')


def vminstances(request):
    if request.method == "POST":
        # base = zstack_base_demo.zstack_base_api()
        page_start = int(request.POST.get('iDisplayStart'))
        page_end = page_start + 20
        # page_start = int(request.POST.get('iDisplayStart'))
        # new_zs = zstack_VM_api.zstack_vminstance_api(base)
        # vm_list = VmsInfo.query()

        current_vm = vm_list[page_start:page_end]
        for vm in current_vm:
            if 'hostUuid' not in vm:
                vm['hostUuid'] = ""
            if 'description' not in vm:
                vm['description'] = ""
            if len(vm.get('description')) >= 11:
                vm['description'] = vm['description'][:11] + '...'
            memorySize = vm.get('memorySize') / 1024 / 1024 / 1024
            vm['memorySize'] = round(memorySize, 2)
        data = {
            "iTotalRecords": len(vm_list),
            "iTotalDisplayRecords": len(vm_list),
            "aaData": current_vm
        }

        return HttpResponse(json.dumps(data))
    if request.method == "GET":
        base = zstack_base_demo.zstack_base_api()
        new_zs = zstack_VM_api.zstack_vminstance_api(base)
        vm_list = new_zs.query_all_vm()
        for vms in vm_list:
            query_return = VmsInfo.query_vms(**vms)
            if len(query_return) != 0:
                vms['vmNics'] = vms.get('vmNics')[0].get('ip')
                vms['lastOpDate'] = " "
                vms['allVolumes'] = " "
                VmsInfo.update_vms(**vms)
            else:
                vms['vmNics'] =vms.get('vmNics')[0].get('ip')
                vms['lastOpDate'] = " "
                vms['allVolumes'] = " "
                VmsInfo.add_vms(**vms)
        global vm_list
        return render(request, 'order/vminstances.html')

    """