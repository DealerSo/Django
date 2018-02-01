from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    context = {'name': 'home page..', 'list': range(10)}
    return render(request, 'homepage/index.html', context)
