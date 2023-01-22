from rest_framework import serializers
from ChatApp.models import *
from EmailApp.models import *
from EventApp.models import *
from TodoApp.models import *
from django.contrib.auth.models import User

# For user serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'