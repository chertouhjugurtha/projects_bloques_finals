
from rest_framework import serializers

from .models import Ministere

class MinistereSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ministere
        fields = ('__all__')