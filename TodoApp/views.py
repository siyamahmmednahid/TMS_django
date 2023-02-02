from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *
from django.contrib.auth.models import User

# For Todo list and create API
class TodoListCreateAPI(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()

    def list(self, request, *args, **kwargs):
        user = request.user
        serializer = TodoDetailSerializer(self.get_queryset().order_by('-id'), many=True)

        if user.is_superuser:
            return Response({
                'status': True, 
                'message': 'Todo list', 
                'data': serializer.data})
        else:
            todos = []
            for todo in serializer.data:
                if todo['user'] == user.id or todo['Assignee'] == user.id:
                    todos.append(todo)
            return Response({
                'status': True, 
                'message': 'Todo list', 
                'data': todos})


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





# For Todo detail, update and delete API
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

            if request.user.is_superuser or request.user == todo.user:
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
            elif request.user == todo.Assignee:
                serializer = TodoAssigneeSerializer(todo, data=request.data)
                if todo.Completed == True:
                    return Response({
                        'status': False, 
                        'message': 'Todo already completed'})
                else:
                    if serializer.is_valid():
                        serializer.save()
                        serializer = TodoAssigneeSerializer(serializer.instance)
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