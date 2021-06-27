from rest_framework import serializers

from .models import DataTarif, Tarif


class TarifSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tarif
        fields = "__all__"


class DataTarifSerializer(serializers.ModelSerializer):
    data_tarifs = TarifSerializer(many=True, required=False)

    class Meta:
        model = DataTarif
        fields = "__all__"
