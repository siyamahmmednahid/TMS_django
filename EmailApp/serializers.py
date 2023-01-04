from rest_framework import serializers
from .models import *



# For sender
class SenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['Receiver', 'CarbonCopy', 'BlindCarbonCopy', 'Subject', 'Body']



class SenderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['id', 'Receiver', 'CarbonCopy', 'BlindCarbonCopy', 'Subject', 'Body', 'Date', 'SenderLabel', 'SenderDraft', 'SenderImportant', 'SenderTrash', 'SenderDelete']





# For receiver
class ReceiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['Sender', 'CarbonCopy', 'BlindCarbonCopy', 'Subject', 'Body']


class ReceiverDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['Sender', 'CarbonCopy', 'BlindCarbonCopy', 'Subject', 'Body', 'Date', 'ReceiverLabel', 'ReceiverDraft', 'ReceiverImportant', 'ReceiverTrash', 'ReceiverDelete']





# For carbon copy
class CarbonCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['Sender', 'Receiver', 'BlindCarbonCopy', 'Subject', 'Body']


class CarbonCopyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['Sender', 'Receiver', 'BlindCarbonCopy', 'Subject', 'Body', 'Date', 'CarbonCopyLabel', 'CarbonCopyDraft', 'CarbonCopyImportant', 'CarbonCopyTrash', 'CarbonCopyDelete']





# For blind carbon copy
class BlindCarbonCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['Sender', 'Receiver', 'CarbonCopy', 'Subject', 'Body']


class BlindCarbonCopyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['Sender', 'Receiver', 'CarbonCopy', 'Subject', 'Body', 'Date', 'BlindCarbonCopyLabel', 'BlindCarbonCopyDraft', 'BlindCarbonCopyImportant', 'BlindCarbonCopyTrash', 'BlindCarbonCopyDelete']