from django.contrib import admin
from .models import Task,Context,List
# Register your models here.
admin.site.register(List)
admin.site.register( Context)
admin.site.register(Task )