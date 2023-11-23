from .models import Films
from rest_framework import serializers


class FilmsSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Films
        exclude = ['genre', 'direct']


