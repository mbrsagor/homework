from django.urls import path

from .views import (
    TaskPostView, TaskDetailsViews, AddTaskView
)

urlpatterns = [
    path('task/', TaskPostView.as_view(), name='tasks'),
    path('task/<int:id>/', TaskDetailsViews.as_view(), name='task-details'),
    path('add-tasks/', AddTaskView.as_view(), name='create-task'),
]
