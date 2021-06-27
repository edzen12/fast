from rest_framework import viewsets, mixins

from .serializers import LinkPriceSerializer
from .models import LinkPrice


class LinkPriceViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = LinkPrice.objects.all()
    serializer_class = LinkPriceSerializer