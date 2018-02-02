from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^barcamp/$', views.BarcampList.as_view()),
    url(r'^barcamp/(?P<pk>[0-9]+)/$', views.BarcampDetail.as_view()),
    url(r'^talk/$', views.TalkList.as_view()),
    url(r'^talk/(?P<pk>[0-9]+)/$', views.TalkDetail.as_view()),
    url(r'^speaker/$', views.SpeakerList.as_view()),
    url(r'^speaker/(?P<pk>[0-9]+)/$', views.SpeakerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
