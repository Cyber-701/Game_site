from django.shortcuts import render

# Create your views here.


def game1(request):
    return render(request, 'game1.html')

def game2(request):
    return render(request, 'game2.html')

def game3(request):
    return render(request, 'game3.html')

def settings(request):
    return render(request, 'settings.html')

def home(request):
    return render(request, 'home.html')