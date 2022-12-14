from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import *
from .models import *
from django.contrib.auth.models import User


# For email list and create API
class EmailListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

    def get_queryset(self):
        user = self.request.user
        return Email.objects.filter(user=user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = EmailDetailSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user)
        serializer = EmailSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=user)
            return Response({'message': 'Email created successfully', 'data': serializer.data})
        else:
            return Response({'message': 'Something went wrong', 'data': serializer.errors})
