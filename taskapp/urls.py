from django.conf.urls import patterns, url

from taskapp import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^(?P<category_id>\d+)/$', views.category, name='category'),
  url(r'^(?P<category_id>\d+)/(?P<project_id>\d+)/$', views.project, name='project'),
)
