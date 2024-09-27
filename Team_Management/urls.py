# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('team_management_handler/', views.team_management_handler,name='team_management_handler'),
]
