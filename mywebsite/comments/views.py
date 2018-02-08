from django.shortcuts import render

# Create your views here.


def addComments(request):
    return render(request, 'comments/addComments.html')


def listComments(request):
    pass