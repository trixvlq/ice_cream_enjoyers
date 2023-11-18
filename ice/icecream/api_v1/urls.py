from django.urls import path
from .views import *
urlpatterns = [
    path('ice_creams/',IceCreamApiList.as_view(),name='icecreams'),
    path('ice_creams/<slug:slug>/',IceCreamUpdate.as_view(),name='update'),
    path('ice_creams_delete/<slug:slug>/',IceCreamDelete.as_view(),name='delete'),
    path('ice_creams_create/',IceCreamCreate.as_view(),name='create'),
]