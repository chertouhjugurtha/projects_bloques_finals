

from rest_framework import serializers

from debloqueur.models import Debloqueur

class DebloqueurSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debloqueur
        fields = ('__all__')