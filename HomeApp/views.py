from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User


# For user list API
class UserListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        serializer = UserSerializer(User.objects.all(), many=True)
        return Response({
            'status': True, 
            'message': 'User list', 
            'data': serializer.data})
