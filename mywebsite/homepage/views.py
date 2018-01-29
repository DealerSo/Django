from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def start(request):
    return HttpResponse('Hello,Django...')

def index(request):
    context = {'name' : 'home page..'}
    return render(request,'homepage/index.html',context)