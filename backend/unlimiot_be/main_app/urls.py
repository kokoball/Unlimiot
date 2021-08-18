from django.contrib import admin
from django.urls import path, include
from .views import index, main

urlpatterns = [
    path('', index, name='index'),
    path('front', main, name='mainPage_1'),
]
