from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventListCreateAPIView.as_view()),
    path('<int:pk>/', views.EventDetailAPIView.as_view()),
]