from django.urls import path

from contacts.views.auth_view import RegisterApiView

urlpatterns = [
    path('register', RegisterApiView.as_view()),
]
