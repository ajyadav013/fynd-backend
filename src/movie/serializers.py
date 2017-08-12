"""
Movie serializer
"""
from rest_framework import serializers
from django.conf import settings
from .models import (Movie, Genre)

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name')
        
class MovieSerializer(serializers.ModelSerializer):    
    genres = GenreSerializer(many=True)
    class Meta:
        model= Movie
        fields = ('id', 'name', 'popularity', 'genres', 'director', 'imdbScore')

