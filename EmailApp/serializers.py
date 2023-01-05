from rest_framework import serializers
from .models import *



# For sender 
class SenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['Receiver', 'Cc', 'Bcc', 'Subject', 'Body']


class SenderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'Receiver', 'Cc', 'Bcc', 'Subject', 'Body']



# For receiver
class ReceiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['Sender', 'Cc', 'Bcc', 'Subject', 'Body']


class ReceiverDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'Sender', 'Cc', 'Bcc', 'Subject', 'Body']