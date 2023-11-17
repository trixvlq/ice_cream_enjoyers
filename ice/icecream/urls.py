from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', index,name='home'),
    path('users/',include('users.urls')),
    path('icecream/<slug:slug>/',icecream,name='icecream'),
    path('search/',search,name="search"),
    path('favorite/<slug:slug>/',favorite,name='favorite'),
    path('delete/<slug:slug>/',delete_ice_cream,name='delete'),
    path('edit/<slug:slug>/',change_ice_cream,name='edit'),
    path('trending/',trending,name='trending'),
    path('create/',add_ice,name='create'),
    path('favorites/',favorites,name='favorites'),
    path('my-ice-creams/',my_ice_creams,name='my_ice_creams'),
]
