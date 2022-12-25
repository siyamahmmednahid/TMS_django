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
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

    def list(self, request, *args, **kwargs):
        if request.user.is_superuser:
            queryset = Todo.objects.all()
        else:
            queryset = Todo.objects.filter(user=request.user)
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        user = request.user
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response({'status': True, 'message': 'Todo created successfully', 'data': serializer.data})
        else:
            return Response({'status': False, 'message': 'Todo not created', 'data': serializer.errors})


class TodoDetailAPI(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoDetailSerializer
    queryset = Todo.objects.all()

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = TodoDetailSerializer(instance)
    #     return Response(serializer.data)
    def retrieve(self, request, pk):
        try:
            todo = Todo.objects.get(id=pk)
            serializer = TodoDetailSerializer(todo)
            return Response({'status': True, 'message': 'Todo Detail', 'data': serializer.data})
        except Todo.DoesNotExist:
            return Response({'status': False, 'message': 'Todo does not exist'})

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.is_superuser:
            serializer = TodoSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True, 'message': 'Todo updated successfully', 'data': serializer.data})
            else:
                return Response({'status': False, 'message': 'Todo not updated', 'data': serializer.errors})
        else:
            serializer = TodoAssigneeSerializer(instance, data=request.data)
            if Todo.objects.filter(Completed=True).exists():
                return Response({'status': False, 'message': 'Todo is completed'})
            else:
                if serializer.is_valid():
                    serializer.save()
                    return Response({'status': True, 'message': 'Todo updated successfully', 'data': serializer.data})
                else:
                    return Response({'status': False, 'message': 'Todo not updated', 'data': serializer.errors})