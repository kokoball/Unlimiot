from django.shortcuts import render


def index(request):
    return render(request, 'main_app/nearShopPage_1.html')

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