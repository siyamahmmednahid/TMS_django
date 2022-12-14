from django.urls import path
from . import views

urlpatterns = [
    path('', views.ChatList.as_view(), name='chat_list'),
]