from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmailListAPIView.as_view()),
    # path('sent/', views.SentEmailListCreateAPIView.as_view()),
    # path('<int:pk>/', views.EmailDetailUpdateDeleteAPIView.as_view())
]