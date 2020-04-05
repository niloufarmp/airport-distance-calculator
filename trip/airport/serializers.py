from rest_framework import serializers

from airport.models import DistanceComputeResponse


class DistanceComputeResponseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DistanceComputeResponse
        fields = ('first_airport_code', 'second_airport_code', 'distance')
