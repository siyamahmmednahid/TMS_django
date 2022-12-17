from django.urls import path, include
from .views import *

urlpatterns = [
    # path('register/', UserRegistrationApi.as_view()),
    # path('signin/', SingInAPI.as_view()),
    path('signin/', UserSignInApi.as_view()),
    path('signup/', UserSignUpApi.as_view()),
    path('change-password/', ChangePasswordApi.as_view()),
    # path('forgot-password/', UserPasswordForgotApi.as_view()),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]