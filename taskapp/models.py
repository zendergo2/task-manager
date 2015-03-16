from datetime import datetime
from django.db import models
from django.utils.text import slugify 

# Create your models here.

class Category (models.Model):
  # A category, or a collection of tasks and projects.
  # who are in turn collections of tasks
  
  title       = models.CharField(max_length = 200)
  description = models.CharField(max_length = 200, default = "Add a description...")
  
  def __unicode__ (self):
    return self.title

class Task (models.Model):
  # A task, or one thing that needs to get done
  # if it can be done in one sitting, or if it
  # doesn't need to keep track of progress.
  
  title       = models.CharField(max_length = 200)
  category    = models.ForeignKey(Category)
  start_date  = models.DateTimeField('date to start', default = datetime.now())
  due_date    = models.DateTimeField('date to end')
  description = models.CharField(max_length = 200, default = "Add a description...")
  
  def __unicode__ (self):
    return self.title

class Project (models.Model):
  # A project, or a collection of tasks
  # needing to be worked on more than once

  title       = models.CharField(max_length = 200)
  category    = models.ForeignKey(Category)
  start_date  = models.DateTimeField('date to start', default = datetime.now())
  due_date    = models.DateTimeField('date to end')
  description = models.CharField(max_length = 200, default = "Add a description...")

  def __unicode__(self):
    return self.title

class Project_Task (models.Model):
  # A task for a project. Separate from a regular
  # task in memory because it is not tied to a
  # category, but a project.

  title       = models.CharField(max_length = 200)
  project     = models.ForeignKey(Project)
  start_date  = models.DateTimeField('date to start', default = datetime.now())
  due_date    = models.DateTimeField('date to end')
  description = models.CharField(max_length = 200, default = "Add a description...")

  def __unicode__(self):
    return self.title
