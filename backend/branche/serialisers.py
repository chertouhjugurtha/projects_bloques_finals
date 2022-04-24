
from rest_framework import serializers

from .models import Branche

class BrancheSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branche
        fields = ('__all__')