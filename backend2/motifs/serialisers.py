
from rest_framework import serializers

from .models import Motifs

class MotifsSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motifs
        fields = ('__all__')