from django.contrib import admin
from .models import (Movie, Genre)

class GenreAdmin(admin.ModelAdmin):
    """
    Genre admin
    """
    pass

class MovieAdmin(admin.ModelAdmin):
    """
    Movie admin
    """
    pass




admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
