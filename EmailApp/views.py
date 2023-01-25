from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView
from .serializers import *
from .models import *
from django.contrib.auth.models import User



# For email list and email update API
class EmailListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = request.user
        queryset = Email.objects.filter(Receiver=user, ReceiverDelete=False)
        CcQueryset = Email.objects.filter(Cc=user, CcDelete=False)
        BccQueryset = Email.objects.filter(Bcc=user, BccDelete=False)
        serializer = ReceiverSerializer(queryset, many=True)
        ccSerializer = CcSerializer(CcQueryset, many=True)
        bccSerializer = BccSerializer(BccQueryset, many=True)
        return Response({
            'status': True,
            'message': 'Email list',
            'Receiver': serializer.data,
            'Cc': ccSerializer.data,
            'Bcc': bccSerializer.data})





# For email detail and email update API
class EmailDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk):
        try:
            user = request.user
            if Email.objects.filter(id=pk, Receiver=user, ReceiverDelete=False).exists():
                queryset = Email.objects.get(id=pk, Receiver=user)
                serializer = ReceiverSerializer(queryset)
                return Response({
                    'status': True,
                    'message': 'Receiver email detail',
                    'data': serializer.data})
            elif Email.objects.filter(id=pk, Cc=user, CcDelete=False).exists():
                queryset = Email.objects.get(id=pk, Cc=user)
                serializer = CcSerializer(queryset)
                return Response({
                    'status': True,
                    'message': 'Cc email detail',
                    'data': serializer.data})
            elif Email.objects.filter(id=pk, Bcc=user, BccDelete=False).exists():
                queryset = Email.objects.get(id=pk, Bcc=user)
                serializer = BccSerializer(queryset)
                return Response({
                    'status': True,
                    'message': 'Bcc email detail',
                    'data': serializer.data})
            else:
                return Response({
                    'status': False,
                    'message': 'Email not found'})
        except:
            return Response({
                'status': False,
                'message': 'Email not found'})

    def update(self, request, pk):
        try:
            user = request.user
            data = request.data      
            if Email.objects.filter(id=pk, Receiver=user).exists():
                queryset = Email.objects.get(id=pk, Receiver=user)
                serializer = ReceiverUpdateSerializer(queryset, data=data)
                if serializer.is_valid():
                    serializer.save()
                    serializer = ReceiverSerializer(serializer.instance)
                    return Response({
                        'status': True,
                        'message': 'Receiver email updated successfully',
                        'data': serializer.data})
                else:
                    return Response({
                        'status': False,
                        'message': 'Receiver email not updated',
                        'data': serializer.errors})
            elif Email.objects.filter(id=pk, Cc=user).exists():
                queryset = Email.objects.get(id=pk, Cc=user)
                serializer = CcUpdateSerializer(queryset, data=data)
                if serializer.is_valid():
                    serializer.save()
                    serializer = CcSerializer(serializer.instance)
                    return Response({
                        'status': True,
                        'message': 'Cc email updated successfully',
                        'data': serializer.data})
                else:
                    return Response({
                        'status': False,
                        'message': 'Cc email not updated',
                        'data': serializer.errors})
            elif Email.objects.filter(id=pk, Bcc=user).exists():
                queryset = Email.objects.get(id=pk, Bcc=user)
                serializer = BccUpdateSerializer(queryset, data=data)
                if serializer.is_valid():
                    serializer.save()
                    serializer = BccSerializer(serializer.instance)
                    return Response({
                        'status': True,
                        'message': 'Bcc email updated successfully',
                        'data': serializer.data})
                else:
                    return Response({
                        'status': False,
                        'message': 'Bcc email not updated',
                        'data': serializer.errors})
            else:
                return Response({
                    'status': False,
                    'message': 'Email not found'})
        except:
            return Response({
                'status': False,
                'message': 'Email not found'})

    def destroy(self, request, pk):
        try:
            user = request.user
            if Email.objects.filter(id=pk, Receiver=user).exists():
                queryset = Email.objects.get(id=pk, Receiver=user)
                if queryset.ReceiverTrash == True:
                    queryset.ReceiverDelete = True
                    queryset.save()
                    return Response({
                        'status': True,
                        'message': 'Receiver email deleted successfully'})
                else:
                    return Response({
                        'status': False,
                        'message': 'Receiver email not in trash'})
            elif Email.objects.filter(id=pk, Cc=user).exists():
                queryset = Email.objects.get(id=pk, Cc=user)
                if queryset.CcTrash == True:
                    queryset.CcDelete = True
                    queryset.save()
                    return Response({
                        'status': True,
                        'message': 'Cc email deleted successfully'})
                else:
                    return Response({
                        'status': False,
                        'message': 'Cc email not in trash'})
            elif Email.objects.filter(id=pk, Bcc=user).exists():
                queryset = Email.objects.get(id=pk, Bcc=user)
                if queryset.BccTrash == True:
                    queryset.BccDelete = True
                    queryset.save()
                    return Response({
                        'status': True,
                        'message': 'Bcc email deleted successfully'})
                else:
                    return Response({
                        'status': False,
                        'message': 'Bcc email not in trash'})
            else:
                return Response({
                    'status': False,
                    'message': 'Email not found'})
        except:
            return Response({
                'status': False,
                'message': 'Email not found'})





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





# For draft email resend API
class DraftEmailResendAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk):
        try:
            user = request.user
            email = Email.objects.get(id=pk)
            serializer = SentEmailSerializer(email)
            if email.Sender == user:
                return Response({
                    'status': True,
                    'message': 'Draft email detail',
                    'data': serializer.data})
            else:
                return Response({
                    'status': False,
                    'message': 'You are not the sender of this email'})
        except:
            return Response({
                'status': False,
                'message': 'Email not found'})
        
    def update(self, request, pk):
        try:
            user = request.user
            email = Email.objects.get(id=pk)
            data = request.data
            serializer = SentEmailSerializer(email, data=data)
            if serializer.is_valid():
                serializer.save()
                serializer = SentEmailDetailSerializer(serializer.instance)
                return Response({
                    'status': True,
                    'message': 'Draft email sent successfully',
                    'data': serializer.data})
            else:
                return Response({
                    'status': False,
                    'message': 'Draft email not sent',
                    'data': serializer.errors})
        except:
            return Response({
                'status': False,
                'message': 'Email not found'})
    




# For sent email detail, update and delete API
class SentEmailDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk):
        try:
            user = request.user
            email = Email.objects.get(id=pk)
            serializer = SentEmailDetailSerializer(email)
            if email.Sender == user:
                if email.SenderDelete == True:
                    return Response({
                        'status': False,
                        'message': 'Sent email deleted'})
                else:
                    return Response({
                        'status': True,
                        'message': 'Sent email detail',
                        'data': serializer.data})
            else:
                return Response({
                    'status': False,
                    'message': 'You are not the sender of this email'})
        except:
            return Response({
                'status': False,
                'message': 'Email not found'})

    def update(self, request, pk):
        try:
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
                        'message': 'Sent email updated successfully',
                        'data': serializer.data})
                else:
                    return Response({
                        'status': False,
                        'message': 'Sent email not updated'})
            else:
                return Response({
                    'status': False,
                    'message': 'You are not the sender of this email'})
        except:
            return Response({
                'status': False,
                'message': 'Email not found'})

    def destroy(self, request, pk):
        try:
            user = request.user
            email = Email.objects.get(id=pk)
            if email.Sender == user:
                if email.SenderTrash == True:
                    email.SenderDelete = True
                    email.save()
                    return Response({
                        'status': True,
                        'message': 'Sent email deleted successfully'})
                else:
                    return Response({
                        'status': False,
                        'message': 'Sent email not in trash'})
            else:
                return Response({
                    'status': False,
                    'message': 'You are not the sender of this email'})
        except:
            return Response({
                'status': False,
                'message': 'Email not found'})