from django.urls import reverse
from rest_framework import serializers

from tasks.models import ListModel, TaskModel


class ListsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListModel
        fields = '__all__'
        exclude = []

    list_details_url = serializers.SerializerMethodField()

    def get_list_details_url(self, obj):
        request = self.context.get('request')
        if request is not None:
            track_listing_url = request.build_absolute_uri(reverse('list_all_tasks', args=[obj.slug]))
            return track_listing_url
        return None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['list_details_url'] = data.pop('list_details_url')
        return data





class TasksForListSerializer(serializers.ModelSerializer):
    # track_listing = serializers.HyperlinkedIdentityField(view_name='task_details',lookup_field='id',)

    class Meta:
        model = TaskModel
        exclude = []


    task_details_url = serializers.SerializerMethodField()

    def get_task_details_url(self, obj):
        request = self.context.get('request')
        if request is not None:
            track_listing_url = request.build_absolute_uri(reverse('task_details', args=[obj.related_list.slug,obj.pk]))
            return track_listing_url
        return None


    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['task_details_url'] = data.pop('task_details_url')
        return data





class ListTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListModel
        fields = '__all__'
        exclude = []


    tasks=TasksForListSerializer(many=True)
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['tasks'] = data.pop('tasks')
        return data




class relatedListForTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListModel
        fields = '__all__'
        exclude = []

    list_url = serializers.SerializerMethodField()

    def get_list_url(self, obj):
        request = self.context.get('request')
        if request is not None:
            track_listing_url = request.build_absolute_uri(
                reverse('list_all_tasks', args=[obj.slug]))
            return track_listing_url
        return None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['list_url'] = data.pop('list_url')
        return data





class TaskSerializer(serializers.ModelSerializer):
    related_list = relatedListForTaskSerializer()

    class Meta:
        model = TaskModel
        fields = '__all__'
        exclude = []

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['related_list'] = data.pop('related_list')
        return data

