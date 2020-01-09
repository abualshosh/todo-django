from django.db import models
from django.utils import timezone
# Create your models here.

class List(models.Model):
    name = models.CharField(max_length=255)

class Context(models.Model):
    context_name = models.CharField(max_length=255)

class Task(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='list', blank=False, null=False)
    context= models.ForeignKey(Context, on_delete=models.CASCADE, related_name='context',blank=False, null=False)
    task_text = models.CharField(max_length=255)
    is_complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

