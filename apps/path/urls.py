from django.urls import path
from .views import get_path

app_name = 'path'

urlpatterns = [
    path('find/', get_path, name='find-path'),
]
