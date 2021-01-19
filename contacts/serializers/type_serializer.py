from rest_framework.serializers import ModelSerializer
from contacts.models.types import Type


class TypeSerializer(ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'title', 'color', 'is_active', 'created_at', 'updated_at')
