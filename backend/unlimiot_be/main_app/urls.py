from django.contrib import admin
from django.urls import path, include
from .views import nsp, mainp, nsp, cdp1, cdp2, ips, ip1, mrs, sp1

urlpatterns = [
    path('', nsp, name='nsp'),
    path('front', mainp, name='mainp'),
    path('nsp', nsp, name='nsp'),
    path('cdp1', cdp1, name='cdp1'),
    path('cdp2', cdp2, name='cdp2'),
    path('ips', ips, name='ips'),
    path('ip1', ip1, name='ip1'),
    path('mrs', mrs, name='mrs'),
    path('sp1', sp1, name='sp1'),
]
