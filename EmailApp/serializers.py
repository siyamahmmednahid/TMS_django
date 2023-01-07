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
        fields = ['SenderLabel', 'SenderImportant', 'SenderTrash']


class SentEmailDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['id', 'Receiver', 'Cc', 'Bcc', 'Subject', 'Body', 'Date', 'Draft', 'SenderLabel', 'SenderImportant', 'SenderTrash', 'SenderDelete']




# For receiver
class ReceiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['id', 'Sender', 'Receiver', 'Cc', 'Subject', 'Body', 'Date', 'ReceiverLabel', 'ReceiverImportant', 'ReceiverTrash', 'ReceiverDelete']


class ReceiverUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['ReceiverLabel', 'ReceiverImportant', 'ReceiverTrash']





# For Cc
class CcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['id', 'Sender', 'Receiver', 'Cc', 'Subject', 'Body', 'Date', 'CcLabel', 'CcImportant', 'CcTrash', 'CcDelete']


class CcUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['CcLabel', 'CcImportant', 'CcTrash']





# For Bcc
class BccSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['id', 'Sender', 'Receiver', 'Cc', 'Subject', 'Body', 'Date', 'BccLabel', 'BccImportant', 'BccTrash', 'BccDelete']


class BccUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['BccLabel', 'BccImportant', 'BccTrash']