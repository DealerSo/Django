from django.shortcuts import render
from django.http import HttpResponse
from homepage.models import Student


# Create your views here.


def start(request):
    return HttpResponse('Hello,Django...')


def index(request):
    context = {'name': 'home page..'}
    return render(request, 'homepage/index.html', context)


def findAll(request):
    students = Student.objects.all()
    content = {'students': students}
    return render(request, 'homepage/studentList.html', content)


def getDetail(request):
    fid = request.GET.get('id')
    student = Student.objects.get(id=fid)
    content = {'student': student}
    return render(request, 'homepage/studentDetail.html', content)
