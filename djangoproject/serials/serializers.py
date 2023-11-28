from .models import Serials
from rest_framework import serializers


class SerialsSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Serials
        fields = ['title', 'genre', 'is_favorite']

class SerialsDetailSerializer(serializers.ModelSerializer):

    genre = serializers.StringRelatedField(many=True)
    director = serializers.StringRelatedField(many=True)
    class Meta:
        model = Serials
        fields = '__all__'