from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
  # Examples:
  # url(r'^$', 'tasks.views.home', name='home'),
  # url(r'^blog/', include('blog.urls')),
  
  url(r'^tasks/', include('taskapp.urls', namespace="taskapp")),
  url(r'^admin/', include(admin.site.urls)),
)
