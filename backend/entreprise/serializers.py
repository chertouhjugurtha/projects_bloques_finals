from .models import Entreprise
from rest_framework import serializers
class EntrepriseSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entreprise
        fields = ('__all__')