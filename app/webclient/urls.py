from django.urls import path
from . import views
from webclient.views import home
from webclient.views import places_list
from webclient.views import base
from webclient.views import place
from webclient.views import  pay_page

urlpatterns = [
    path('', home, name='home'),
    path('city/<int:city_id>', places_list, name='city'),
    path('base', base, name='base'),
    path('place/<int:place_id>', place, name='place'),
    path('pay_page/<int:place_id>', pay_page, name='pay_page'),
]