from django.shortcuts import render
from article.models import Article, ArticleEncoder
# 导入分页包
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.core import serializers


# Create your views here.

# 实现分页效果
def listArticles(request):
    # 请求参数 pageIndex 页数
    pageIndex = request.GET.get('pageIndex')
    # 请求参数 pageCount 每页显示多少条记录
    # pageCount = request.GET.get('pageCount')
    pageCount = 10

    # (1) Article.objects.filter 参数增加过滤条件 status=1
    # (2) 使用objects.filter需要加上排序，否则下一行代码会报警告，这里按照id升序排列，如果写错'-id'表示倒序排列
    # UnorderedObjectListWarning: Pagination may yield inconsistent results with an unordered object_list
    articles_list = Article.objects.filter(status=1).order_by('id')

    # 获得分页对象
    paginator = Paginator(articles_list, pageCount)

    # 对象可分几页
    pageSize = paginator.num_pages
    pageRange = range(1, pageSize + 1)
    try:
        # 获取pageIndex页中的内容,比如：pageIndex为1,那么就获取第一页中的内容
        articles = paginator.page(pageIndex)
    except PageNotAnInteger:
        print('pageIndex param is not Integer type.')
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(pageSize)

    context = {'pageRange': pageRange, 'articles': articles}

    return render(request, 'article/articleList.html', context)


# 查询文章明细
def articleDetail(request):
    pid = request.GET.get('id')

    article = Article.objects.filter(id=pid)

    # 序列化
    result = serializers.serialize("json", article)

    return HttpResponse(result)
