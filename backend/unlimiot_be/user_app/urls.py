from django.contrib import admin
from django.urls import path, include
from .views import indexD, LoginView, mypage

urlpatterns = [
    # .. 중략 ..
    path('', indexD),
    path('login', LoginView.as_view()),
    path('mypage', mypage),
    # path('dd/signup/', SignupView.as_view()),
    # path('dd/logout/', LogoutView.as_view()),
]
