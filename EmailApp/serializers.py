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
        fields = ['id', 'Sender', 'Receiver', 'Cc', 'Subject', 'Body', 'Date', 'Draft', 'ReceiverLabel', 'ReceiverImportant', 'ReceiverRead', 'ReceiverTrash', 'ReceiverDelete']


class ReceiverUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['ReceiverRead', 'ReceiverLabel', 'ReceiverImportant', 'ReceiverTrash']





# For Cc
class CcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['id', 'Sender', 'Receiver', 'Cc', 'Subject', 'Body', 'Date', 'Draft', 'CcLabel', 'CcImportant', 'CcRead', 'CcTrash', 'CcDelete']


class CcUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['CcLabel', 'CcImportant', 'CcRead', 'CcTrash']





# For Bcc
class BccSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['id', 'Sender', 'Receiver', 'Cc', 'Subject', 'Body', 'Date', 'Draft', 'BccLabel', 'BccImportant', 'BccRead', 'BccTrash', 'BccDelete']


class BccUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['BccLabel', 'BccImportant', 'BccRead', 'BccTrash']