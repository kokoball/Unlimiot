from django.contrib import admin
from django.urls import path, include
from .views import history

urlpatterns = [
    path('history/', history, name='history'),
    #path('<int:pk>', main, name='mainPage_1'),
]
