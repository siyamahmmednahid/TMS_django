from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import generics
from django.contrib.auth.models import User
from django_rest_passwordreset.views import ResetPasswordRequestToken





# For User Sign In API
class UserSignInAPI(TokenObtainPairView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        data = request.data
        username = data['username']
        password = data['password']

        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            if user.check_password(password):
                token = super().post(request, format=None)
                return Response({
                    'status': True,
                    'message': 'User logged in successfully',
                    'access': token.data['access'],
                    'refresh': token.data['refresh'],
                    'data': {
                        'id': user.id,
                        'username': user.username,
                        'email': user.email,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'is_active': user.is_active,
                        'is_staff': user.is_staff,
                        'is_superuser': user.is_superuser
                    }
                })
            else:
                return Response({
                    'status': False,
                    'message': 'Wrong credentials'
                })
        else:
            return Response({
                'status': False,
                'message': 'Wrong credentials'
            })





# For User Sign Up API
class UserSignUpAPI(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    def post(self, request, format=None):
        data = request.data
        username = data['username']
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        password1 = data['password1']
        password2 = data['password2']

        def validate_password(password):
            if len(password) < 8:
                return False
            if password.isnumeric():
                return False
            if password.isalpha():
                return False
            return True

        if request.user.is_superuser or request.user.is_staff:
            if User.objects.filter(username=username).exists():
                return Response({
                    'status': False,
                    'message': 'Username already exists'
                })
            elif User.objects.filter(email=email).exists():
                return Response({
                    'status': False,
                    'message': 'Email already exists'
                })
            elif not validate_password(password1):
                return Response({
                    'status': False,
                    'message': 'Password must be at least 8 characters long and must contain at least one letter and one number'
                })
            elif password1 != password2:
                return Response({
                    'status': False,
                    'message': 'Password does not match'
                })
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
                user.save()
                return Response({
                    'status': True,
                    'message': 'User created successfully',
                    'data': {
                        'username': username,
                        'name': first_name + ' ' + last_name,
                        'email': email,
                        'password': password1
                    }
                })
        else:
            return Response({
                    'status': False,
                    'message': 'You are not authorized to create a user'
                })





# For Change Password API
class ChangePasswordAPI(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    def put(self, request, format=None):
        data = request.data
        old_password = data['old_password']
        new_password1 = data['new_password1']
        new_password2 = data['new_password2']

        def validate_password(password):
            if len(password) < 8:
                return False
            if password.isnumeric():
                return False
            if password.isalpha():
                return False
            return True

        if request.user.check_password(old_password):
            if not validate_password(new_password1):
                return Response({
                    'status': False,
                    'message': 'Password must be at least 8 characters long and must contain at least one letter and one number'
                })
            elif new_password1 != new_password2:
                return Response({
                    'status': False,
                    'message': 'Password does not match'
                })
            else:
                user = User.objects.get(username=request.user.username)
                user.set_password(new_password1)
                user.save()
                return Response({
                    'status': True,
                    'message': 'Password changed successfully'
                })
        else:
            return Response({
                'status': False,
                'message': 'Wrong credentials'
            })