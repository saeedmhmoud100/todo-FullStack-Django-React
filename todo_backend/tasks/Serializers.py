from rest_framework import serializers

from tasks.models import ListModel, TaskModel




class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        exclude = []


class ListSerializer(serializers.ModelSerializer):
    # task = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = ListModel
        fields='__all__'
        exclude = []