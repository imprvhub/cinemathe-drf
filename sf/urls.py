# sf/urls.py
from django.urls import path

from sf.views import index


urlpatterns = [
    path('', index),
]