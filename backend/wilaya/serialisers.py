
from rest_framework import serializers

from .models import Wilaya

class WilayaSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wilaya
        fields = ('__all__')