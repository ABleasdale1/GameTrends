# Baby urls.py
# Path: GameTrends/gameTrends/userApp/urls.py

from django.urls import path
from . import views

app_name = 'userApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('friends/', views.friends, name='friends'),
    path('store/', views.store, name='store'),
]