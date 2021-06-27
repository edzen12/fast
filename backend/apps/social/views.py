from rest_framework import viewsets, mixins

from .serializers import SocialSerializer, ReviewsSerializer
from .models import Social, Reviews


class SocialViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer


class ReviewsViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer