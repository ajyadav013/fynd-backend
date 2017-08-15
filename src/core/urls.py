"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import (url, include)
from django.views.static import serve
from django.conf import settings
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from movie.views import (MovieViewSet, GenreViewSet)

router = DefaultRouter()

router.register(r'movies', MovieViewSet, base_name="Movie")
router.register(r'genres', GenreViewSet, base_name="Genre") 


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth', include('authentication.urls')),
    url(r'^social', include('social.urls')),
    url(r'', include(router.urls)),
]
if not settings.DEBUG:
    urlpatterns += [url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}), ]
