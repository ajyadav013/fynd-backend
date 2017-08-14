"""
Movie serializer
"""
from django.db import transaction  
from django.conf import settings

from rest_framework import serializers

from .models import (Movie, Genre)

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'
        
class MovieSerializer(serializers.ModelSerializer):    
    genres = GenreSerializer(many=True)
    class Meta:
        model= Movie
        fields = ('id', 'name', 'popularity', 'genres', 'director', 'imdbScore')

    @transaction.atomic
    def create(self, validated_data):
        print('Inside create')
        genres_data = validated_data.pop('genres')
        movie = Movie.objects.create(**validated_data)
        for genre_data in genres_data:
            genre = Genre.objects.filter(name=genre_data.get('name')).first()
            movie.genres.add(genre)
        return movie

    @transaction.atomic
    def update(self, instance, validated_data):
        genres = validated_data['genres']
        instance.name = validated_data['name']
        instance.popularity = validated_data['popularity']
        instance.director = validated_data['director']
        instance.imdbScore = validated_data['imdbScore']
        instance.save()
        movie = Movie.objects.get(id=instance.id)
        for genre_data in genres: 
           genre = Genre.objects.filter(name=genre_data.get('name')).first()
           #print('Genre ', genre[0].id)
           #instance.genres.add(genre)
           movie.genres.add(genre)
        movie.save()
        print('instance genres', instance.genres)
        print('movie genres', movie.genres)
        return instance
