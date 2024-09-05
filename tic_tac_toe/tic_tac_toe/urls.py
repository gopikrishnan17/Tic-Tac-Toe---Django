"""
URL configuration for tic_tac_toe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from single_player.views import *
from multi_player.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home, name = 'home'),
    path('play/', play, name = 'play'),
    path('game/', tictactoe, name='tictactoe'),
    path('singlewindetails/', singlewindetails, name='singlewindetails'),
    path('make_move/', make_move, name='make_move'),
    path('restart_game/', restart_game, name='restart_game'),
    path('contact/', contact_page, name='contact_page'),
    path('about/', about_page, name='about_page'),
    path('' , include('multi_player.urls')),
]
