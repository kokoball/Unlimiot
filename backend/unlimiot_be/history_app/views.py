from django.shortcuts import render


def history(request):
    return render(request, 'history_app/history.html')


# Create your views here.
