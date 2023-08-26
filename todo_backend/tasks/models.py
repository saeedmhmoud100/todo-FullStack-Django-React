from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now


# Create your models here.
class Utilitys(models.Model):
    title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=True)

    class Meta:
        abstract=True

    def __str__(self):
        return self.title


class ListModel(Utilitys):
    slug = models.CharField(unique=True,default='',max_length=30,null=True,blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class TaskModel(Utilitys):
    related_list = models.ForeignKey(ListModel,related_name='tasks',null=True, on_delete=models.CASCADE)
    isDone = models.BooleanField(default=False)
