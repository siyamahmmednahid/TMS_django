from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import ListAPIView


# For user list API
class UserListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    