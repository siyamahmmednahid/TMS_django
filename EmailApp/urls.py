from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmailListAPIView.as_view()),
    path('<int:pk>/', views.EmailDetailAPIView.as_view()),
    path('sent/', views.SentEmailListAPIView.as_view()),
    path('sent/<int:pk>/', views.SentEmailDetailAPIView.as_view()),
    path('draft/<int:pk>/', views.DraftEmailResendAPIView.as_view()),
]