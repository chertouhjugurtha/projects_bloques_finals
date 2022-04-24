
from rest_framework import serializers

from .models import Commune

class CommuneSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commune
        fields = ('__all__')