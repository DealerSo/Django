from django.conf.urls import url
import homepage.views

urlpatterns = [
    url('^index', homepage.views.index)
]
