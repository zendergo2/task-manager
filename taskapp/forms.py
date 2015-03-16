from django.forms import ModelForm
from taskapp.models import Category, Task, Project, Project_Task

class AddCategoryForm (ModelForm):
  class Meta:
    model  = Category
    fields = ['title',]

class AddTaskForm (ModelForm):
  class Meta:
    model  = Task
    fields = ['title', 'category', 'due_date',]

class AddProjectForm (ModelForm):
  class Meta:
    model  = Project
    fields = ['title', 'category', 'due_date',]

class AddProjectTaskForm (ModelForm):
  class Meta:
    model  = Project_Task
    fields = ['title', 'project', 'due_date',]

