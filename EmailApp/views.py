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
        # user = request.user
        # queryset = (Email.objects.all().filter(Receiver=user).order_by('-Date')) | (Email.objects.all().filter(Sender=user).order_by('-Date')) | (Email.objects.all().filter(CarbonCopy=user).order_by('-Date')) | (Email.objects.all().filter(BlindCarbonCopy=user).order_by('-Date'))
        # receiver = ReceiverDetailSerializer(queryset, many=True)
        # sender = SenderDetailSerializer(queryset, many=True)
        # cc = CarbonCopyDetailSerializer(queryset, many=True)
        # bcc = BlindCarbonCopyDetailSerializer(queryset, many=True)
        # return Response({
        #     'status': True,
        #     'message': 'Email list',
        #     'sender': sender.data,
        #     'receiver': receiver.data,
        #     'cc': cc.data,
        #     'bcc': bcc.data})
        user = request.user
        if user == Email.objects.all().filter(Receiver=user):
            queryset = Email.objects.all().filter(Receiver=user).order_by('-Date')
            serializer = ReceiverDetailSerializer(queryset, many=True)
            return Response({
                'status': True,
                'message': 'Email list',
                'data': serializer.data})
        elif user == Email.objects.all().filter(Sender=user):
            queryset = Email.objects.all().filter(Sender=user).order_by('-Date')
            serializer = SenderDetailSerializer(queryset, many=True)
            return Response({
                'status': True,
                'message': 'Email list',
                'data': serializer.data})
        elif user == Email.objects.all().filter(CarbonCopy=user):
            queryset = Email.objects.all().filter(CarbonCopy=user).order_by('-Date')
            serializer = CarbonCopyDetailSerializer(queryset, many=True)
            return Response({
                'status': True,
                'message': 'Email list',
                'data': serializer.data})
        elif user == Email.objects.all().filter(BlindCarbonCopy=user):
            queryset = Email.objects.all().filter(BlindCarbonCopy=user).order_by('-Date')
            serializer = BlindCarbonCopyDetailSerializer(queryset, many=True)
            return Response({
                'status': True,
                'message': 'Email list',
                'data': serializer.data})
        else:
            return Response({
                'status': False,
                'message': 'Email list not found'})


    def create(self, request, *args, **kwargs):
        serializer = SenderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(Sender=request.user)
            serializer = SenderDetailSerializer(serializer.instance)
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
class EmailDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk):
        try:
            email = Email.objects.get(pk=pk)
            if request.user == email.Sender:
                serializer = SenderDetailSerializer(email)
                return Response({
                    'status': True, 
                    'message': 'Email detail', 
                    'data': serializer.data})
            elif request.user == email.Receiver:
                serializer = ReceiverDetailSerializer(email)
                return Response({
                    'status': True, 
                    'message': 'Email detail', 
                    'data': serializer.data})
            elif request.user == email.CarbonCopy:
                serializer = CarbonCopyDetailSerializer(email)
                return Response({
                    'status': True, 
                    'message': 'Email detail', 
                    'data': serializer.data})
            elif request.user == email.BlindCarbonCopy:
                serializer = BlindCarbonCopyDetailSerializer(email)
                return Response({
                    'status': True, 
                    'message': 'Email detail', 
                    'data': serializer.data})
            else:
                return Response({
                    'status': False, 
                    'message': 'You are not authorized to view this email'})
        except Email.DoesNotExist:
            return Response({
                'status': False, 
                'message': 'Email not found'})

#     def update(self, request, pk):
#         try:
#             email = Email.objects.get(pk=pk)

#             if request.user == email.Sender or request.user == email.Receiver:
#                 serializer = EmailUpdateSerializer(email, data=request.data)
#                 if serializer.is_valid():
#                     serializer.save()
#                     serializer = EmailDetailSerializer(serializer.instance)
#                     return Response({
#                         'status': True, 
#                         'message': 'Email updated successfully', 
#                         'data': serializer.data})
#                 else:
#                     return Response({
#                         'status': False, 
#                         'message': 'Email not updated', 
#                         'data': serializer.errors})
#             else:
#                 return Response({
#                     'status': False, 
#                     'message': 'You are not allowed to update this email'})
#         except Email.DoesNotExist:
#             return Response({
#                 'status': False, 
#                 'message': 'Email not found'})

#     def destroy(self, request, pk):
#         try:
#             email = Email.objects.get(pk=pk)

#             if request.user == email.Receiver:
#                 if email.Deleted == True:
#                     email.Receiver = None
#                     email.save()
#                     return Response({
#                         'status': True,
#                         'message': 'Email deleted successfully'})
#                 else:
#                     return Response({
#                         'status': False,
#                         'message': 'Email not deleted. You can only delete email from trash'})
#             else:
#                 return Response({
#                     'status': False, 
#                     'message': 'You are not allowed to delete this email'})
#         except Email.DoesNotExist:
#             return Response({
#                 'status': False, 
#                 'message': 'Email not found'})