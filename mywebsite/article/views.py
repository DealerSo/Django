from django.shortcuts import render
from article.models import Article


# Create your views here.


def getArticles(request):
    articles = Article.objects.all()
    content = {'articles': articles}
    return render(request, 'article/articleList.html', content)
