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
        model = Movie
        fields = ('id', 'name', 'popularity',
                  'genres', 'director', 'imdbScore')

    @transaction.atomic
    def create(self, validated_data):
        genres_data = validated_data.pop('genres')
        movie = Movie.objects.create(**validated_data)
        for genre_data in genres_data:
            genre = Genre.objects.filter(name=genre_data.get('name')).first()
            movie.genres.add(genre)
        return movie

    @transaction.atomic
    def update(self, instance, validated_data):
        print('validated data', validated_data)
        genres = validated_data['genres']
        instance.name = validated_data['name']
        instance.popularity = validated_data['popularity']
        instance.director = validated_data['director']
        instance.imdbScore = validated_data['imdbScore']
        instance.save()
        genre = []
        for genre_data in genres:
            genre.append(Genre.objects.filter(
                name=genre_data.get('name')).first())
        instance.genres.set(genre)
        return instance
