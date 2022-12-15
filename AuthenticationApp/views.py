from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import generics
from rest_framework import status
from .serializers import *
from django.contrib.auth.models import User



# For User Sign Up API
class UserSignUpApi(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None):
        data = request.data
        username = data['username']
        email = data['email']
        password1 = data['password1']
        password2 = data['password2']

        if request.user.is_superuser:
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
            elif password1 != password2:
                return Response({
                    'status': False,
                    'message': 'Password does not match'
                })
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                return Response({
                    'status': True,
                    'message': 'User created successfully',
                    'data': {
                        'username': username,
                        'email': email,
                        'password': password1
                    }
                })
        else:
            return Response({
                    'status': False,
                    'message': 'You are not authorized to create a user'
                })



# For User Sign In API
class UserSignInApi(TokenObtainPairView):
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
                    'message': 'Wrong password'
                })
        else:
            return Response({
                'status': False,
                'message': 'Wrong username'
            })





# For Change Password API
class ChangePasswordApi(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    model = User
    serializer_class = ChangePasswordSerializer

    def get_object(self, queryset = None):
        obj = self.request.user
        return obj


    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': {
                    'id': self.object.id,
                    'username': self.object.username,
                    'email': self.object.email,
                    'first_name': self.object.first_name,
                    'last_name': self.object.last_name,
                    'is_active': self.object.is_active,
                    'is_staff': self.object.is_staff,
                    'is_superuser': self.object.is_superuser,
                    'password': serializer.data.get("new_password")
                }
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# For User Password Forgot API









# User Registration API
# class UserRegistrationApi(APIView):
#     permission_classes = [AllowAny]
#     def post(self, request, format=None):
#         username = request.data['username']
#         first_name = request.data['first_name']
#         last_name = request.data['last_name']
#         email = request.data['email']
#         password1 = request.data['password1']
#         password2 = request.data['password2']

#         if User.objects.filter(username=username).exists():
#             return Response({'status': False,'message': 'Username already exists'})
#         elif User.objects.filter(email=email).exists():
#             return Response({'status': False,'message': 'Email already exists'})
#         elif password1 != password2:
#             return Response({'status': False,'message': 'Passwords do not match'})
#         else:
#             user = User()
#             user.username = username
#             user.first_name = first_name
#             user.last_name = last_name
#             user.email = email
#             user.is_active = True
#             user.set_password(password1)
#             user.save()
#             return Response(
#                 {
#                     'status': True, 
#                     'message': 'User created successfully', 
#                     'data': {
#                         'username': username, 
#                         'password': password1
#                     }
#                 }
#             )



# User Sign In API
# class SingInAPI(TokenObtainPairView):
#     permission_classes = [AllowAny]
#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)
#         data = response.data
#         data['user_id'] = User.objects.get(username=request.data['username']).id
#         data['username'] = request.data['username']
#         data['first_name'] = User.objects.get(username=request.data['username']).first_name
#         data['last_name'] = User.objects.get(username=request.data['username']).last_name
#         data['email'] = User.objects.get(username=request.data['username']).email
#         data['is_active'] = User.objects.get(username=request.data['username']).is_active
#         data['is_staff'] = User.objects.get(username=request.data['username']).is_staff
#         data['is_superuser'] = User.objects.get(username=request.data['username']).is_superuser
#         return Response(
#             {
#                 'status': True,
#                 'message': 'User logged in successfully',
#                 'data': data
#             }
#         )