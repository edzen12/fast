from rest_framework import serializers

from .models import PayImage


class PayImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PayImage
        fields = "__all__"
        