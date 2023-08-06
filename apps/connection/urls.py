from django.urls import path
from .views import get_path

app_name = 'connection'

urlpatterns = [
    path('find-path/', get_path, name='find-path'),
]
