from rest_framework import viewsets, mixins

from .serializers import PayImageSerializer
from .models import PayImage


class PayImageViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = PayImage.objects.all()
    serializer_class = PayImageSerializer