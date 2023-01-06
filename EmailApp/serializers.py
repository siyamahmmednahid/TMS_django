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
        fields = ['id', 'Sender', 'Cc', 'Subject', 'Body', 'Date']


class ReceiverUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['ReceiverLabel', 'ReceiverImportant', 'ReceiverTrash', 'ReceiverDelete']


class ReceiverDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['id', 'Sender', 'Cc', 'Subject', 'Body', 'Date', 'ReceiverLabel', 'ReceiverImportant', 'ReceiverTrash', 'ReceiverDelete']





# For Cc
class CcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['id', 'Sender', 'Receiver', 'Subject', 'Body', 'Date']


class CcUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['CcLabel', 'CcImportant', 'CcTrash', 'CcDelete']


class CcDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['id', 'Sender', 'Receiver', 'Subject', 'Body', 'Date', 'CcLabel', 'CcImportant', 'CcTrash', 'CcDelete']





# For Bcc
class BccSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['id', 'Sender', 'Receiver', 'Subject', 'Body', 'Date']


class BccUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['BccLabel', 'BccImportant', 'BccTrash', 'BccDelete']


class BccDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['id', 'Sender', 'Receiver', 'Cc', 'Subject', 'Body', 'Date', 'BccLabel', 'BccImportant', 'BccTrash', 'BccDelete']