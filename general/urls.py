from django.urls import path
from .views import *

app_name = 'general'

urlpatterns = [
    path('', main_cover, name='main_page'),
]
