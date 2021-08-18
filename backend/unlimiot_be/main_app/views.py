from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
import datetime
import json


f = open("static/chabka_data.csv", 'r', encoding='UTF8')
l = []
lines = f.readlines()
for line in lines:
    l.append(line.split(','))
f.close()

data1 = l[1:15]


def mainp(request):
    return render(request, 'main_app/mainPage_1.html', {'data1':data1})


def nsp(request):
    return render(request, 'main_app/nearShopPage_1.html')


def cdp1(request):
    return render(request, 'main_app/contentDetailPage_1.html')


def cdp2(request):
    return render(request, 'main_app/contentDetailPage_2.html')


def ips(request):
    return render(request, 'main_app/indexPageStart.html')


def ip1(request):
    return render(request, 'main_app/indexPage_1.html')


def mrs(request):
    return render(request, 'main_app/mainRegionSelectionPage_1.html')


def sp1(request):
    return render(request, 'main_app/searchPage_1.html')



# # Create your views here.
# def index(request):
#     return render(request, 'main_app/index.html', {'data1':data1})