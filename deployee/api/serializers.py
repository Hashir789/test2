from rest_framework.serializers import ModelSerializer
from ..models import ABC
class ABCSerializer(ModelSerializer):
    class Meta:
        model = ABC
        fields = ['id', 'ab', 'bc']