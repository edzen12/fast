from rest_framework import viewsets, mixins

from apps.contact.models import FormEmail
from apps.contact.serializers import FormEmailSerializer


class FormEmailViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = FormEmail.objects.all()
    serializer_class = FormEmailSerializer