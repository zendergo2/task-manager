from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404

from taskapp.models import Category, Project
from taskapp.forms import AddCategoryForm, AddTaskForm, AddProjectForm, AddProjectTaskForm

def index (request):
  category_list = Category.objects.order_by('title')
  category_form = AddCategoryForm(request.POST or None)

  if request.method == 'POST':
    if category_form.is_valid():
      category_form.save()
    return HttpResponseRedirect(reverse('taskapp:index'))

  return render(request, 'taskapp/index.html', \
    {'category_list': category_list, 'category_form': category_form,})

def category (request, category_id):
  category     = get_object_or_404(Category, pk=category_id)
  task_form    = AddTaskForm(request.POST or None)
  project_form = AddProjectForm(request.POST or None)

  if request.method == 'POST':
    if task_form.is_valid():
      task_form.save()

    if project_form.is_valid():
      project_form.save()
    
    return HttpResponseRedirect(reverse('taskapp:category', \
      kwargs={'category_id': category_id,}))

  return render(request, 'taskapp/category.html', \
    {'category': category, 'task_form': task_form, 'project_form': project_form})

def project (request, category_id, project_id):
  category = get_object_or_404(Category, pk=category_id)
  project = get_object_or_404(Project, pk=project_id)
  project_task_form = AddProjectTaskForm(request.POST or None)

  if request.method == 'POST':
    if project_task_form.is_valid():
      project_task_form.save()
    return HttpResponseRedirect(reverse('taskapp:project', \
      kwargs={'category_id': category_id, 'project_id': project_id,}))

  return render(request, 'taskapp/project.html', \
    {'category': category, 'project': project, 'project_task_form': project_task_form})
