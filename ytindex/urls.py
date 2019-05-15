from django.urls import path, re_path
from .views import default, search

urlpatterns = [
    path('search/', default),
    re_path('search/(?P<index>\w*)/(?P<query>.*)', search, name='search'),
]
