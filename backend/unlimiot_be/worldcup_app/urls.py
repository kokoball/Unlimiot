from django.contrib import admin
from django.urls import path, include
from .views import like_style, style_1, style_2, style_3, style_4, style_5, style_6

urlpatterns = [
    path('like_style', like_style, name='like_style'),
    path('style_1', style_1, name='style_1'),
    path('style_2', style_2, name='style_2'),
    path('style_3', style_3, name='style_3'),
    path('style_4', style_4, name='style_4'),
    path('style_5', style_5, name='style_5'),
    path('style_6', style_6, name='style_6'),
    #path('<int:pk>', main, name='mainPage_1'),
]
