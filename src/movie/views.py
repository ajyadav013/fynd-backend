from rest_framework.views import APIView
from rest_framework.settings import api_settings
from rest_framework.permissions import (IsAuthenticated, )
from rest_framework import viewsets
#from rest_framework.response import Response  
from django.http import HttpResponse
from .models import (Movie, Genre)
from .serializers import (MovieSerializer, GenreSerializer)


class GenreViewSet(viewsets.ModelViewSet):
    """
    Genre ViewSet for all genres
    """
    authentication_classes = api_settings.DEFAULT_AUTHENTICATION_CLASSES
    permission_classes = (IsAuthenticated, )
    serializer_class = GenreSerializer 

    def get_queryset(self):
        return Genre.objects.all()


class MovieViewSet(viewsets.ModelViewSet):
    """
    Movie View to return all movies
    """
    #authentication_classes = api_settings.DEFAULT_AUTHENTICATION_CLASSES
    #permission_classes = (IsAuthenticated, )
    serializer_class = MovieSerializer 

    def get_queryset(self):
        return Movie.objects.prefetch_related('genres').all()
