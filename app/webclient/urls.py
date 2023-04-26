from django.urls import path
from . import views
from webclient.views import home
from webclient.views import places_list
from webclient.views import base
from webclient.views import place

urlpatterns = [
    path('', home, name='home'),
    path('places_list', places_list, name='places_list'),
    path('base', base, name='base'),
     path('place', place, name='place'),
]