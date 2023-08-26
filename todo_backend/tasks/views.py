from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from tasks.Serializers import ListsSerializer, ListTasksSerializer
from tasks.models import ListModel


# Create your views here.

@api_view(['GET'])
def all_list_view(request):
    if(request.method=='GET'):
        Lists = ListsSerializer(ListModel.objects.all(),many=True,context={'request': request})
        return Response(Lists.data)

@api_view(['GET'])
def list_tasks_view(request,slug):
    if(request.method=='GET'):
        List = ListTasksSerializer(ListModel.objects.filter(slug=slug),many=True,context={'request': request})
        return Response(List.data)

