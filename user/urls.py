
from unicodedata import name
from .views import BlacklistTokenUpdateView, MyTokenObtainPairView, customUserCreate
from django.contrib import admin
from django.urls import path,include

from rest_framework_simplejwt.views import (
    
    TokenRefreshView,
)

urlpatterns = [
   path('register/',customUserCreate.as_view(),name='create_user'),
   path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('logout/',BlacklistTokenUpdateView.as_view(),name='logout_user')
]
