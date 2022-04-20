
from django.contrib import admin
from django.urls import path

from api.views import birthdayAPI


urlpatterns = [
   path('details/<int:userid>',birthdayAPI.as_view()),
   path('details/',birthdayAPI.as_view()),

   path('details/<int:userid>/<int:pk>',birthdayAPI.as_view())
]
