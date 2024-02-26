from rest_framework.viewsets import ModelViewSet
from ..models import ABC
from .serializers import ABCSerializer

class ABCViewSet(ModelViewSet):
    queryset = ABC.objects.all()
    serializer_class = ABCSerializer