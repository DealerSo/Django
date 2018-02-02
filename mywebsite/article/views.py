from django.shortcuts import render
from article.models import Article
# 导入分页包
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

# 实现分页效果
def listArticles(request):
    # 请求参数 pageIndex 页数
    pageIndex = request.GET.get('pageIndex')
    # 请求参数 pageCount 每页显示多少条记录
    # pageCount = request.GET.get('pageCount')
    pageCount = 10

    # Article.objects.filter 参数增加过滤条件 status=1
    articles_list = Article.objects.filter(status=1)

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

    content = {'pageRange': pageRange, 'articles': articles}

    return render(request, 'article/articleList.html', content)
