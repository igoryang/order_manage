# -*- encoding:utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse

# Create your views here.

# def index(request):
#     return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'order.html')