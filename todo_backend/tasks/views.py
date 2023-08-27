from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from tasks.Serializers import TaskSerializer
from tasks.models import TaskModel


@api_view(['GET'])
def all_tasks_view(request):
    if(request.method=='GET'):
        task = TaskSerializer(TaskModel.objects.all(),many=True,context={'request': request})
        return Response(task.data)

