from rest_framework import viewsets, mixins

from .serializers import ServiceSerializer
from .models import Service


class ServiceViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer