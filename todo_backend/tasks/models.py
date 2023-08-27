from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now



class TaskModel(models.Model):
    title = models.CharField(max_length=30)
    isDone = models.BooleanField(default=False,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=True)
    def __str__(self):
        return self.title