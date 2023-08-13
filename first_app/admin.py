from django.contrib import admin
from . models import TaskModel
# Register your models here.


class TaskModelAdmin(admin.ModelAdmin):
    list_display = ('Task_Title', 'Task_Description', 'Status')


admin.site.register(TaskModel, TaskModelAdmin)
