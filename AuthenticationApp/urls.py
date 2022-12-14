from django.urls import path
from .views import *

urlpatterns = [
    # path('register/', UserRegistrationApi.as_view()),
    # path('signin/', SingInAPI.as_view()),
    path('signin/', UserSignInApi.as_view()),
    path('signup/', UserSignUpApi.as_view()),
]