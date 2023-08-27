from django.contrib import admin

from tasks.models import TaskModel


# Register your models here.

# @admin.register(ListModel)
# class ListModelAdmin(admin.ModelAdmin):
#     exclude = ['slug']


@admin.register(TaskModel)
class ListModelAdmin(admin.ModelAdmin):
    pass