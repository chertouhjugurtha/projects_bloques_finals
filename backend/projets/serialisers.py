
from rest_framework import serializers

from .models import Projects

class projectsSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('__all__')