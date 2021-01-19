from django.urls import path
from rest_framework.routers import DefaultRouter

from contacts.views.auth_view import RegisterApiView
from contacts.views.type_view import TypeViewSet

router = DefaultRouter()
router.register('types', TypeViewSet)

urlpatterns = [
    path('register', RegisterApiView.as_view()),
] + router.urls
