from django.urls import path
from .views import get_path, test

app_name = 'connection'

urlpatterns = [
    path('find-path/', get_path, name='find-path'),
    path('test/', test, name='test')
]
