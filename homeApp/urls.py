from django.urls import path

from .views import *

urlpatterns = [
    path('task/', TaskPostView.as_view(), name='tasks'),
    path('task/<int:id>/', TaskDetailsViews.as_view(), name='task-details'),
    path('tasks/', AddTaskView.as_view(), name='create-task'),
    path('tasks/<int:id>/', AddTaskRetrieveView.as_view(), name='tasks-details'),
]
