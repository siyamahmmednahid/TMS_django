from rest_framework import serializers
from .models import *

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        field = '__all__'
        exclude = ['Sender']


class ChatDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'