"""
Movie Model
"""
from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '%s'%(self.name)
    
class Movie(models.Model):
    """
    Social platform user model
    """
    name = models.CharField(max_length=500)
    popularity = models.DecimalField(max_digits=3, decimal_places=1)
    director = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre, related_name='movies')
    imdbScore = models.DecimalField(max_digits=2, decimal_places=1)

    
    def __str__(self):
        return '%s'%(self.name)

    
