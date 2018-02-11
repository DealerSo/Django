from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from comments.models import Comments
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def addComments(request):
    return render(request, 'comments/addComments.html')


@csrf_exempt
def saveComments(request):
    ######################################保存留言--开始######################################
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    sex = request.POST['sex']
    title = request.POST['title']
    content = request.POST['content']
    # 当前时间
    now = datetime.datetime.now()
    comments = Comments(name=name, email=email, phone=phone, sex=sex, title=title, content=content, createdTime=now)
    comments.save();
    ######################################保存留言--结束######################################

    ######################################查看留言--开始######################################

    # 默认为第1页，显示10条记录
    pageIndex = 1
    pageCount = 10
    context = getComments(pageIndex, pageCount)

    return render(request, 'comments/listComments.html', context)
    ######################################查看留言--结束######################################


def listComments(request):
    pageIndex = request.GET.get('pageIndex')
    pageCount = 10
    context = getComments(pageIndex, pageCount)

    return render(request, 'comments/listComments.html', context)



# 获取comments数据公共方法
def getComments(pageIndex, pageCount):
    comments_list = Comments.objects.filter(status=1).order_by('-id')

    # 获得分页对象
    paginator = Paginator(comments_list, pageCount)

    # 对象可分几页
    pageSize = paginator.num_pages
    # 前端显示的页数
    pageRange = range(1, pageSize + 1)

    try:
        comments = paginator.page(pageIndex)
    except PageNotAnInteger:
        print('pageIndex param is not Integer type.')
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(pageSize)

    context = {'pageRange': pageRange, 'comments': comments}

    return context
