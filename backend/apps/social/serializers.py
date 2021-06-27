from rest_framework import serializers

from .models import Social, Reviews


class SocialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Social
        fields = "__all__"


class ReviewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reviews
        fields = "__all__"