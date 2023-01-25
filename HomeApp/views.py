from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User
from .serializers import *


# For user list API
class UserListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        serializer = UserSerializer(User.objects.all(), many=True)
        return Response({
            'status': True, 
            'message': 'User list', 
            'data': serializer.data})
    




# For todo list API
class TodoListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        serializer = TodoSerializer(Todo.objects.all(), many=True)
        return Response({
            'status': True, 
            'message': 'Teacher rank list', 
            'data': serializer.data})
    




# For supervisor list API
class SupervisorTodoListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = request.user
        serializer = SupervisorTodoSerializer(Todo.objects.filter(user=user), many=True)
        return Response({
            'status': True,
            'message': 'Me as Supervisor list',
            'data': serializer.data})
    




# For teacher list API
class MyTodoListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = request.user
        serializer = TodoSerializer(Todo.objects.filter(Assignee=user), many=True)
        return Response({
            'status': True,
            'message': 'My task list',
            'data': serializer.data})
    




# For event list API
class EventListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        serializer = EventSerializer(Event.objects.all(), many=True)
        return Response({
            'status': True, 
            'message': 'Event list', 
            'data': serializer.data})