from rest_framework import serializers
from .models import *

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'


class EmailDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'
        exclude = ['Sender']