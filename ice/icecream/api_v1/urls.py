from django.urls import path
from .views import *
urlpatterns = [
    path('ice_creams/',IceCreamApiList.as_view(),name='icecreams'),
    path('ice_creams/<slug:slug>/',IceCreamUpdate.as_view(),name='update'),
]