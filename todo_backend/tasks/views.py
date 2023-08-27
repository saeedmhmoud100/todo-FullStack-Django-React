from rest_framework import status, serializers
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

@api_view(['GET','DELETE',"PUT","PATCH"])
def task_details_view(request,pk):
    try:
        task = TaskModel.objects.get(pk=pk)
        if(request.method=='GET'):
                serializer = TaskSerializer(task, context={'request': request})
                return Response(serializer.data)
        elif(request.method=="DELETE"):
            task.delete()
            return Response({'status': "deleted"}, status=status.HTTP_200_OK)
        elif(request.method == "PUT" or request.method=="PATCH"):
            serializer = TaskSerializer(task,data=request.data, context={'request': request})
            if(serializer.is_valid()):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    except TaskModel.DoesNotExist:
        return Response({'status':"not found"},status=status.HTTP_404_NOT_FOUND)

    return Response(status=status.HTTP_400_BAD_REQUEST)

