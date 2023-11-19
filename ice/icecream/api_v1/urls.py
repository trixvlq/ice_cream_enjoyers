from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView, TokenObtainPairView

from .views import *
urlpatterns = [
    path('drf-auth/',include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('ice_creams/',IceCreamApiList.as_view(),name='icecreams'),
    path('ice_creams/<slug:slug>/',IceCreamUpdate.as_view(),name='update'),
    path('ice_creams_delete/<slug:slug>/',IceCreamDelete.as_view(),name='delete'),
    path('ice_creams_create/',IceCreamCreate.as_view(),name='create'),
    path('categories/',CategoryAPIList.as_view(),name='cats'),

]