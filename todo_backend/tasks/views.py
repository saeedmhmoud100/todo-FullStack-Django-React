from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from tasks.Serializers import ListSerializer
from tasks.models import ListModel


# Create your views here.

@api_view(['GET'])
def list_view(request):
    if(request.method=='GET'):
        Lists = ListSerializer(ListModel.objects.all(),many=True)
        return Response(Lists.data)
