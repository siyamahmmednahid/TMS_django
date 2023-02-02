from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *



# For todo create serializer
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


# For todo assignee serializer
class TodoAssigneeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['Important', 'Completed', 'Comment']