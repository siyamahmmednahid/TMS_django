from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import *
from .models import *
from django.contrib.auth.models import User


class ChatList(ListCreateAPIView):
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Chat.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = Chat.objects.filter(Sender=request.user) | Chat.objects.filter(Receiver=request.user)
        serializer = ChatDetailSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(Sender=request.user)
            serializer = ChatDetailSerializer(serializer.instance)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)