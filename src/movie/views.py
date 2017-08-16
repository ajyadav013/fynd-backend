from rest_framework.views import APIView
from rest_framework.settings import api_settings
from rest_framework.permissions import (IsAuthenticated, BasePermission)
from rest_framework import viewsets
#from rest_framework.response import Response
from django.http import HttpResponse
from .models import (Movie, Genre)
from .serializers import (MovieSerializer, GenreSerializer)


class AdminUserPermissions(BasePermission):
    """
    Allow only the Admin to have access to all methods and non-admin has access to only GET method
    """

    def has_permission(self, request, view):
        if not request.user.is_superuser:
            if not request.method == 'GET':
                return False
        return True


class GenreViewSet(viewsets.ModelViewSet):
    """
    Genre ViewSet for all genres
    """
    authentication_classes = api_settings.DEFAULT_AUTHENTICATION_CLASSES
    permission_classes = (IsAuthenticated, AdminUserPermissions)
    serializer_class = GenreSerializer

    def get_queryset(self):
        return Genre.objects.all()


class MovieViewSet(viewsets.ModelViewSet):
    """
    Movie View to create, update, delete movies
    """
    authentication_classes = api_settings.DEFAULT_AUTHENTICATION_CLASSES
    permission_classes = (IsAuthenticated, AdminUserPermissions)
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.prefetch_related('genres').all()
