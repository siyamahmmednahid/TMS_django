from django.urls import path, include
from rest_framework_simplejwt.views import TokenBlacklistView
from .views import *

urlpatterns = [
    path('signin/', UserSignInAPI.as_view()),
    path('signout/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('signup/', UserSignUpAPI.as_view()),
    path('change_password/', ChangePasswordAPI.as_view()),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]