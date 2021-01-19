from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from contacts.models.types import Type
from contacts.serializers.type_serializer import TypeSerializer


class TypeViewSet(ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [IsAuthenticated, ]
