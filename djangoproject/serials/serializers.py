from .models import Serials
from rest_framework import serializers


class SerialsSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Serials
        exclude = ['genre']