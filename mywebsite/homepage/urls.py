from django.conf.urls import url
import homepage.views

urlpatterns = [
    url('^start/', homepage.views.start),
    url('^index/', homepage.views.index)
]