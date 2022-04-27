from django.urls import path
from .views import *

app_name = 'general'

urlpatterns = [
    path('', main_cover, name='main_page'),
    path('table/', tabel_view, name='table'),
    path('import/', trader_txt_import, name='import'),
]
