from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import *
from .models import *
from django.contrib.auth.models import User



# For email list API
class EmailListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = Email.objects.filter(Sender=request.user, SenderDelete=False, SenderTrash=False)
        serializer = SenderSerializer(queryset, many=True)
        return Response(serializer.data)


