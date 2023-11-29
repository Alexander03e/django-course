from .models import Films
from rest_framework import serializers


class FilmsSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Films
        fields = ['title', 'genre', 'is_favorite']

class FilmsDetailSerializer(serializers.ModelSerializer):

    genre = serializers.StringRelatedField(many=True, read_only=True)
    direct = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Films
        fields = '__all__'
