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
        pass





# For sent email and sent email list API
class SentEmailListAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SentEmailSerializer

    def list(self, request, *args, **kwargs):
        user = request.user
        queryset = Email.objects.filter(Sender=user, SenderDelete=False)
        serializer = SentEmailDetailSerializer(queryset, many=True)
        return Response({
            'status': True,
            'message': 'Sent email list',
            'data': serializer.data})

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        serializer = SentEmailSerializer(data=data)
        if serializer.is_valid():
            serializer.save(Sender=user)
            serializer = SentEmailDetailSerializer(serializer.instance)
            return Response({
                'status': True,
                'message': 'Email sent successfully',
                'data': serializer.data})
        else:
            return Response({
                'status': False,
                'message': 'Email not sent',
                'data': serializer.errors})


class SentEmailDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk):
        user = request.user
        email = Email.objects.get(id=pk)
        serializer = SentEmailDetailSerializer(email)
        if email.Sender == user:
            if email.SenderDelete == True:
                return Response({
                    'status': False,
                    'message': 'Email deleted'})
            else:
                return Response({
                    'status': True,
                    'message': 'Email detail',
                    'data': serializer.data})
        else:
            return Response({
                'status': False,
                'message': 'You are not the sender of this email'})

    def update(self, request, pk):
        user = request.user
        data = request.data
        email = Email.objects.get(id=pk)
        serializer = SentEmailUpdateSerializer(email, data=data)
        if email.Sender == user:
            if serializer.is_valid():
                serializer.save()
                serializer = SentEmailDetailSerializer(email)
                return Response({
                    'status': True,
                    'message': 'Email updated',
                    'data': serializer.data})
            else:
                return Response({
                    'status': False,
                    'message': 'Error',
                    'data': serializer.errors})
        else:
            return Response({
                'status': False,
                'message': 'Error',
                'data': 'You are not the sender of this email'})

    def destroy(self, request, pk):
        user = request.user
        email = Email.objects.get(id=pk)
        if email.Sender == user:
            if email.SenderTrash == True:
                email.SenderDelete = True
                email.save()
                return Response({
                    'status': True,
                    'message': 'Email deleted successfully',})
            else:
                return Response({
                    'status': False,
                    'message': 'Email are not in trash',})
        else:
            return Response({
                'status': False,
                'message': 'Error',
                'data': 'You are not the sender of this email'})