
from rest_framework import serializers

from .models import Activite

class ActiviteSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activite
        fields = ('__all__')