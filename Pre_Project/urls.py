from django.urls import path
from . import views


urlpatterns = [    
    path('pre_project_new_handler/', views.pre_project_new_handler, name='pre_project_new_handler'),
]