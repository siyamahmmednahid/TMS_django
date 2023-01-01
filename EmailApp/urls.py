from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmailListCreateAPIView.as_view()),
    path('<int:pk>/', views.EmailDetailUpdateDeleteAPIView.as_view())
]