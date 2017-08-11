from rest_framework.views import APIView
from rest_framework.settings import api_settings
from rest_framework.permissions import (IsAuthenticated, )
from rest_framework import viewsets
#from rest_framework.response import Response  
from django.http import HttpResponse
from .models import Movie
from .serializers import MovieSerializer

class MovieView(viewsets.ModelViewSet):
    """
    Movie View to return all movies
    """
    #authentication_classes = api_settings.DEFAULT_AUTHENTICATION_CLASSES
    #permission_classes = (IsAuthenticated, )
    serializer_class = MovieSerializer 

    def get_queryset(self):
        return Movie.objects.prefetch_related('genres').all()


    def partial_update(self, request, pk=None):
        instance = self.get_object()
        serializer = MovieSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(**serializer.validated_data)
        
