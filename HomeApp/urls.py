from django.urls import path
from . import views

urlpatterns = [
    path('userList/', views.UserListAPIView.as_view()),
    # path('todoList/', views.TodoListAPIView.as_view()),
    path('myTodoList/', views.MyTodoListAPIView.as_view()),
    path('supervisorTodoList/', views.SupervisorTodoListAPIView.as_view()),
    path('eventList/', views.EventListAPIView.as_view()),
    path('teacherRankList/', views.TeacherRankAPIView.as_view()),
    path('userListDropdown/', views.UserDropdownListAPIView.as_view()),
]