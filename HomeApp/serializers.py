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
        fields = ['id', 'is_superuser', 'is_active', 'username', 'first_name', 'last_name', 'email']





# For todo serializer
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'TaskCompleted', 'Assignee']


class SupervisorTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'TaskCompleted', 'user']





# For event serializer
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'EndDateTime']





# For teacher rank serializer
class TeacherRankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'TaskCompleted', 'Assignee']





# For user list dropdown serializer
class UserListDropdownSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'is_superuser']