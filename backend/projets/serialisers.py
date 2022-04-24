
from rest_framework import serializers

from .models import Projets

class projectsSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projets
        fields = ('__all__')