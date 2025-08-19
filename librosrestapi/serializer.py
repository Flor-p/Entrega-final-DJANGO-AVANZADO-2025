from .models import LibrosResApi
from rest_framework import serializers

class LibrosRestApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibrosResApi
        fields = '_all_'
