from rest_framework import viewsets, mixins

from .models import DataTarif
from .serializers import DataTarifSerializer


class TarifViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = DataTarif.objects.all()
    serializer_class = DataTarifSerializer


