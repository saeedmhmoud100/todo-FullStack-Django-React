from django.urls import reverse
from rest_framework import serializers

from tasks.models import TaskModel

#
# class ListsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ListModel
#         fields = '__all__'
#         exclude = []
#
#     list_details_url = serializers.SerializerMethodField()
#
#     def get_list_details_url(self, obj):
#         request = self.context.get('request')
#         if request is not None:
#             track_listing_url = request.build_absolute_uri(reverse('list_all_tasks', args=[obj.slug]))
#             return track_listing_url
#         return None
#
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         data['list_details_url'] = data.pop('list_details_url')
#         return data
#
#


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = '__all__'
        exclude = []
