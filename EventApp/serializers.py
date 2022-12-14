from rest_framework import serializers
from .models import *

# For event add and update serializer
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        field = '__all__'
        exclude = ['user']


# For event detail serializer
class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
