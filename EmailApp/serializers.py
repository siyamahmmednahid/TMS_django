from rest_framework import serializers
from .models import *

# For email list and create API
class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['Receiver', 'CarbonCopy', 'BlindCarbonCopy', 'Subject', 'Body']


# For email detail and delete API
class EmailDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'


# For email update API
class EmailUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['Label', 'Draft', 'Important', 'Read', 'Deleted']


# For email delete API
class EmailDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['Sender', 'Receiver', 'CarbonCopy', 'BlindCarbonCopy']