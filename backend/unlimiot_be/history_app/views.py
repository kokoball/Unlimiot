from django.shortcuts import render


def history(request):
    return render(request, 'history_app/orderHistory.html')


# Create your views here.
