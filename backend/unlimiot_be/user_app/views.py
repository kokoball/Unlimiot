from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as _LoginView, LogoutView as _LogoutView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


def indexD(request):
    return render(request, 'user_app/loginPage_1.html')


class LoginView(_LoginView):
    template_name = "user_app/loginPage_2.html"
    
    
def mypage(request):
    return render(request, 'user_app/myPage_1.html')
    
    
# class SignupView(CreateView):
#     template_name = 'signup.html'
#     form_class = UserCreationForm
#     model = get_user_model()


# class LogoutView(_LogoutView):
#     template_name = "logout.html"

    
# class Profile(DetailView):
#     pass
    
