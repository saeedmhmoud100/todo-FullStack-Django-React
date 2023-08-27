from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from tasks.Serializers import TaskSerializer
from tasks.models import TaskModel


@api_view(['GET'])
def all_tasks_view(request):
    if(request.method=='GET'):
        tasks = TaskSerializer(TaskModel.objects.all(),many=True,context={'request': request})
        return Response(tasks.data)

@api_view(['GET'])
def task_details_view(request,pk):
    if(request.method=='GET'):
        task = TaskSerializer(TaskModel.objects.filter(pk=pk),many=True,context={'request': request})
        return Response(task.data)

