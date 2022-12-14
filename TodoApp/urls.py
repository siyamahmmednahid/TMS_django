from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoListCreateAPI.as_view()),
    path('<int:pk>/', views.TodoDetailAPI.as_view()),
]