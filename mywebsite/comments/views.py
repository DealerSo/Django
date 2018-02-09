from django.shortcuts import render


# Create your views here.


def addComments(request):
    return render(request, 'comments/addComments.html')


def saveComments(request):
    pass


def listComments(request):
    pass
