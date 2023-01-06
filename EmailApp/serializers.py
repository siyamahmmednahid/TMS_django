from rest_framework import serializers
from .models import *



# For sender 
class SentEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['Receiver', 'Cc', 'Bcc', 'Subject', 'Body', 'Draft']


class SentEmailUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['SenderLabel', 'SenderImportant', 'SenderTrash', 'SenderDelete']


class SentEmailDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['id', 'Receiver', 'Cc', 'Bcc', 'Subject', 'Body', 'Date', 'Draft', 'SenderLabel', 'SenderImportant', 'SenderTrash', 'SenderDelete']




# For receiver
class ReceiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['Sender', 'Cc', 'Bcc', 'Subject', 'Body']


class ReceiverDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['id', 'Sender', 'Cc', 'Bcc', 'Subject', 'Body']