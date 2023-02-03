from django.urls import path
from .views import *

urlpatterns = [
    path('', UserListAPI.as_view()),
    path('<int:pk>/', UserDetailAPI.as_view()),


    path('personalinfo/add/', UserPersonalInfoAddAPI.as_view()),
    path('personalinfo/<int:pk>/', UserPersonalInfoAPI.as_view()),


    path('taskCount/<int:pk>/', UserIncompleteTodoCountAPI.as_view()),
    path('emailCount/<int:pk>/', UserUnreadEmailCountAPI.as_view()),
    path('userDeactivate/<int:pk>/', UserDeactivateAPI.as_view()),


    path('academicinfo/', UserAcademicInfoListCreateAPI.as_view()),
    path('academicinfo/<int:pk>/', UserAcademicInfoAPI.as_view()),

    path('traininginfo/', UserTrainingInfoListCreateAPI.as_view()),
    path('traininginfo/<int:pk>/', UserTrainingInfoAPI.as_view()),


    path('teachinginfo/', UserTeachingInfoListCreateAPI.as_view()),
    path('teachinginfo/<int:pk>/', UserTeachingInfoAPI.as_view()),

    path('publicationinfo/', UserPublicationInfoListCreateAPI.as_view()),
    path('publicationinfo/<int:pk>/', UserPublicationInfoAPI.as_view()),


    path('awardscholarshipinfo/', UserAwardAndScholarshipInfoListCreateAPI.as_view()),
    path('awardscholarshipinfo/<int:pk>/', UserAwardAndScholarshipInfoAPI.as_view()),


    path('experienceinfo/', UserExperienceInfoListCreateAPI.as_view()),
    path('experienceinfo/<int:pk>/', UserExperienceInfoAPI.as_view()),
]