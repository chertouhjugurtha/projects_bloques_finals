
from rest_framework import serializers

from .models import Gerant

class GerantSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gerant
        fields = ('__all__')