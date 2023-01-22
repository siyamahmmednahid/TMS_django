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
            'message': 'Todo list', 
            'data': serializer.data})
    


class SupervisorTodoListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = request.user
        serializer = SupervisorTodoSerializer(Todo.objects.filter(user=user), many=True)
        return Response({
            'status': True,
            'message': 'Todo list',
            'data': serializer.data})
    


class MyTodoListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = request.user
        serializer = MyTodoSerializer(Todo.objects.filter(Assignee=user), many=True)
        return Response({
            'status': True,
            'message': 'Todo list',
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