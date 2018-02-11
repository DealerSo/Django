from django.conf.urls import url
import comments.views

urlpatterns = [
    url('^addComments', comments.views.addComments),
    url('^saveComments', comments.views.saveComments),
    url('^listComments', comments.views.listComments)
]
