from django.conf.urls import patterns, url

from taskapp import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^(?P<category_id>\d+)/$', views.category, name='category'),
  url(r'^(?P<category_id>\d+)/(?P<project_id>\d+)/$', views.project, name='project'),

  url(r'^add_category/$', views.add_category, name='add_category'),
  url(r'^add_project/$', views.add_project, name='add_project'),
  url(r'^add_task/$', views.add_task, name='add_task'),
)
