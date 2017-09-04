# -*- encoding:utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
import datetime


# Create your views here.

# def index(request):
#     return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')


def index(request):
    from order import models
    return render(request, 'order.html')

    #
    # def current_datetime(request):
    #     now = datetime.datetime.now()
    #
    #     html_time = "<html><body>Time is %s.</body></html>"% now
    #
    #     return HttpResponse(html_time)


    # def show_index(request):
    #     return render(request, 'show_order.html')
