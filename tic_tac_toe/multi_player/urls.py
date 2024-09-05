from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('createroom/', createroom, name='createroom'),
    path('joinroom/', joinroom, name='joinroom'),
    path('play_multi/<room_code>', play_multi, name = 'play_multi'),
]