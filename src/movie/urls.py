"""
urls for movie
"""

from django.conf.urls import (url)
from .views import (MovieView)

urlpatterns = [
    url(r'', MovieView.as_view({'get':'list'}), name='movies')    
]
