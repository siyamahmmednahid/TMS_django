from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import *
from .models import *
from django.contrib.auth.models import User


# For email list and create API
class EmailListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        queryset = Email.objects.all()
        serializer = EmailDetailSerializer(queryset, many=True)
        return Response({
            'status': True, 
            'message': 'Email list', 
            'data': serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(Sender=request.user)
            serializer = EmailDetailSerializer(serializer.instance)
            return Response({
                'status': True, 
                'message': 'Email created successfully', 
                'data': serializer.data})
        else:
            return Response({
                'status': False, 
                'message': 'Email not created', 
                'data': serializer.errors})
            




# For email detail, update and delete API