from django.conf.urls import url
import article.views

urlpatterns = [
    url('^getArticles/', article.views.getArticles)
]
