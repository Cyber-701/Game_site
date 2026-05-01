from django.shortcuts import render

# Create your views here.


def game1(request):
    return render(request, 'game1.html')

def game2(request):
    return render(request, 'game2.html')
