from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *



# For todo list serializer
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        field = '__all__'
        exclude = ['user', 'Comment', 'TaskCompleted']


# For todo detail serializer
class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'