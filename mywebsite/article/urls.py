from django.conf.urls import url
import article.views

urlpatterns = [
    url('^listArticles', article.views.listArticles),
    url('^articleDetail', article.views.articleDetail)
]
