from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User
from .serializers import *


# For user list API
class UserListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        serializer = UserSerializer(User.objects.all(), many=True)
        return Response({
            'status': True, 
            'message': 'User list', 
            'data': serializer.data})
    




# For todo list API
# class TodoListAPIView(ListAPIView):
#     permission_classes = [IsAuthenticated]

#     def list(self, request, *args, **kwargs):
#         serializer = TodoSerializer(Todo.objects.all(), many=True)
#         return Response({
#             'status': True, 
#             'message': 'Teacher rank list', 
#             'data': serializer.data})
    




# For supervisor list API
class SupervisorTodoListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = request.user
        serializer = SupervisorTodoSerializer(Todo.objects.filter(user=user), many=True)
        return Response({
            'status': True,
            'message': 'Me as Supervisor list',
            'data': serializer.data})
    




# For event list API
class EventListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        serializer = EventSerializer(Event.objects.all(), many=True)
        return Response({
            'status': True, 
            'message': 'Event list', 
            'data': serializer.data})
    




# For teacher list API
class MyTodoListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = request.user
        serializer = TodoSerializer(Todo.objects.filter(Assignee=user), many=True)
        return Response({
            'status': True,
            'message': 'My task list',
            'data': serializer.data})
    




# For teacher rank on completed task API
class TeacherRankAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = User.objects.all().filter(is_active=True).filter(is_superuser=False)
        serializer = TeacherRankSerializer(Todo.objects.all(), many=True)
        
        # Sort user by complete and incomplete task
        user_list = []
        for u in user:
            user_list.append({
                'id': u.id,
                'Name': u.first_name + ' ' + u.last_name,
                'complete_task': 0,
                'incomplete_task': 0
            })

        for u in user_list:
            for s in serializer.data:
                if u['id'] == s['Assignee']:
                    if s['TaskCompleted'] == True:
                        u['complete_task'] += 1
                    else:
                        u['incomplete_task'] += 1

        # Sort user by complete task
        user_list = sorted(user_list, key=lambda k: k['complete_task'], reverse=True)
        return Response({
            'status': True,
            'message': 'Teacher rank list',
            'data': user_list})
    


    




# For user dropdown list API
class UserDropdownListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = User.objects.all().filter(is_active=True)
        serializer = UserListDropdownSerializer(queryset, many=True)
        return Response({
            'status': True,
            'message': 'User list',
            'data': serializer.data})
    