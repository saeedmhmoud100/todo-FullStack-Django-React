from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from tasks.Serializers import TaskSerializer
from tasks.models import TaskModel


@api_view(['GET','POST'])
def all_tasks_view(request):
    if(request.method=='GET'):
        tasks = TaskSerializer(TaskModel.objects.all(),many=True,context={'request': request})
        return Response(tasks.data)
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def task_details_view(request,pk):
    if(request.method=='GET'):
        task = TaskSerializer(TaskModel.objects.filter(pk=pk),many=True,context={'request': request})
        return Response(task.data)

