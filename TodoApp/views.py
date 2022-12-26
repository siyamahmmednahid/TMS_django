from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *
from django.contrib.auth.models import User


class TodoListCreateAPI(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = TodoDetailSerializer(self.get_queryset(), many=True)

        if request.user.is_superuser:
            return Response({
                'status': True, 
                'message': 'Todo list', 
                'data': serializer.data})
        else:
            serializer = TodoDetailSerializer(self.get_queryset().filter(Assignee=request.user), many=True)
            return Response({
                'status': True, 
                'message': 'Todo list', 
                'data': serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            serializer = TodoDetailSerializer(serializer.instance)
            return Response({
                'status': True, 
                'message': 'Todo created successfully', 
                'data': serializer.data})
        else:
            return Response({
                'status': False, 
                'message': 'Todo not created', 
                'data': serializer.errors})



class TodoDetailAPI(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()

    def retrieve(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)

            if request.user.is_superuser or request.user == todo.Assignee:
                serializer = TodoDetailSerializer(todo)
                return Response({
                    'status': True, 
                    'message': 'Todo detail', 
                    'data': serializer.data})
            else:
                return Response({
                    'status': False, 
                    'message': 'You are not authorized to view this todo'})
        except Todo.DoesNotExist:
            return Response({
                'status': False, 
                'message': 'Todo not found'})

    def update(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)

            if request.user.is_superuser or request.user == todo.Assignee:
                serializer = TodoSerializer(todo, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    serializer = TodoDetailSerializer(serializer.instance)
                    return Response({
                        'status': True, 
                        'message': 'Todo updated successfully', 
                        'data': serializer.data})
                else:
                    return Response({
                        'status': False, 
                        'message': 'Todo not updated', 
                        'data': serializer.errors})
            else:
                return Response({
                    'status': False, 
                    'message': 'You are not authorized to update this todo'})
        except Todo.DoesNotExist:
            return Response({
                'status': False, 
                'message': 'Todo not found'})