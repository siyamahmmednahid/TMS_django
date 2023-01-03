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
class EmailDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk):
        try:
            email = Email.objects.get(pk=pk)
            serializer = EmailDetailSerializer(email)
            return Response({
                'status': True, 
                'message': 'Email detail', 
                'data': serializer.data})
        except Email.DoesNotExist:
            return Response({
                'status': False, 
                'message': 'Email not found'})

    def update(self, request, pk):
        try:
            email = Email.objects.get(pk=pk)

            if request.user == email.Sender or request.user == email.Receiver:
                serializer = EmailUpdateSerializer(email, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    serializer = EmailDetailSerializer(serializer.instance)
                    return Response({
                        'status': True, 
                        'message': 'Email updated successfully', 
                        'data': serializer.data})
                else:
                    return Response({
                        'status': False, 
                        'message': 'Email not updated', 
                        'data': serializer.errors})
            else:
                return Response({
                    'status': False, 
                    'message': 'You are not allowed to update this email'})
        except Email.DoesNotExist:
            return Response({
                'status': False, 
                'message': 'Email not found'})

    def destroy(self, request, pk):
        pass





# class EmailDeleteAPIView(DestroyAPIView):
#     def destroy(self, request, pk):
#         try:
#             email = Email.objects.get(pk=pk)

#             if request.user == email.Sender or request.user == email.Receiver:
#                 if email.Deleted == True:
#                     email.delete()
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
