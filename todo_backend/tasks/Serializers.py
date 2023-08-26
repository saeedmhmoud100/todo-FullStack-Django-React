from django.urls import reverse
from rest_framework import serializers

from tasks.models import ListModel, TaskModel


class ListsSerializer(serializers.ModelSerializer):
    # track_listing = serializers.HyperlinkedIdentityField(view_name='list_all_tasks',lookup_field='slug',)
    class Meta:
        model = ListModel
        fields = '__all__'
        exclude = []

    track_listing = serializers.SerializerMethodField()

    def get_track_listing(self, obj):
        request = self.context.get('request')
        if request is not None:
            track_listing_url = request.build_absolute_uri(reverse('list_all_tasks', args=[obj.slug]))
            return track_listing_url
        return None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['track_listing'] = data.pop('track_listing')
        return data


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        exclude = []

class ListTasksSerializer(serializers.ModelSerializer):
    tasks=TaskSerializer(many=True)
    class Meta:
        model = ListModel
        fields = '__all__'
        exclude = []


    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['tasks'] = data.pop('tasks')
        return data

