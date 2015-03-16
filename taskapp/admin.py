from django.contrib import admin

from taskapp.models import Task, Category, Project, Project_Task

# Register your models here.

admin.site.register(Category)
admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Project_Task)
