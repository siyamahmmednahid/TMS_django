from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *



# For todo list serializer
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        field = '__all__'
        exclude = ['user']


# For todo detail serializer
class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


# For todo assignee user serializer
class TodoAssigneeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['Completed', 'Description']