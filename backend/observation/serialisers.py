from rest_framework import serializers

from .models import Observation

class ObservationSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observation
        fields = ('__all__')