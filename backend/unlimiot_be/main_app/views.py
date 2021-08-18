from django.shortcuts import render


def mainp(request):
    return render(request, 'main_app/mainPage_1.html')


def index(request):
    return render(request, 'main_app/mainRegionSelectionPage_1.html')


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

# f = open("static/food.csv", 'r', encoding='UTF8')
# l = []
# lines = f.readlines()
# for line in lines:
#     l.append(line.split(','))
# f.close()

# data1 = l[1:44]

# # Create your views here.
# def index(request):
#     return render(request, 'main_app/index.html', {'data1':data1})