from rest_framework import serializers

from .models import LinkPrice


class LinkPriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = LinkPrice
        fields = "__all__"