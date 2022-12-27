from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import *
from .models import *
from django.contrib.auth.models import User
import json



# For event list and create API
class EventListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        serializer = EventDetailSerializer(Event.objects.all(), many=True)
        return Response({
            'status': True, 
            'message': 'Event list', 
            'data': serializer.data})

    def create(self, request, *args, **kwargs):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            serializer = EventDetailSerializer(serializer.instance)
            return Response({
                'status': True, 
                'message': 'Event created successfully', 
                'data': serializer.data})
        else:
            return Response({
                'status': False, 
                'message': 'Event not created', 
                'data': serializer.errors})





# For event detail, update and delete API
class EventDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
            serializer = EventDetailSerializer(event)
            if request.user.is_superuser or request.user == event.user or request.user in event.Guests.all():
                return Response({
                    'status': True, 
                    'message': 'Event detail', 
                    'data': serializer.data})
            else:
                return Response({
                    'status': False, 
                    'message': 'You are not authorized to view this event'})
        except:
            return Response({
                'status': False, 
                'message': 'Event not found'})

    def update(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
            if request.user.is_superuser or request.user == event.user:
                serializer = EventSerializer(event, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    serializer = EventDetailSerializer(serializer.instance)
                    return Response({
                        'status': True, 
                        'message': 'Event updated successfully', 
                        'data': serializer.data})
                else:
                    return Response({
                        'status': False, 
                        'message': 'Event not updated', 
                        'data': serializer.errors})
            else:
                return Response({
                    'status': False, 
                    'message': 'You are not authorized to update this event'})
        except:
            return Response({
                'status': False, 
                'message': 'Event not found'})

    def destroy(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
            if request.user.is_superuser or request.user == event.user:
                event.delete()
                return Response({
                    'status': True, 
                    'message': 'Event deleted successfully'})
            else:
                return Response({
                    'status': False, 
                    'message': 'You are not authorized to delete this event'})
        except:
            return Response({
                'status': False, 
                'message': 'Event not found'})