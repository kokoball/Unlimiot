from django.contrib import admin
from django.urls import path, include
from .views import nsp, mainp, nsp, cdp1, cdp2, ips, ip1

urlpatterns = [
    path('', nsp, name='index'),
    path('front', mainp, name='mainPage_1'),
    path('nsp', nsp, name='nsp'),
    path('cdp1', cdp1, name='cdp1'),
    path('cdp2', cdp2, name='cdp2'),
    path('ips', ips, name='ips'),
    path('ip1', ip1, name='ip1'),
]
