from django.urls import path
from . import views


urlpatterns = [    
    path('pre_project_new_handler/', views.pre_project_new_handler, name='pre_project_new_handler'),
    path('confirm_project_handler/<id>/', views.confirm_project_handler, name='confirm_project_handler'),
    path('confirm_project_handler/', views.confirm_project_handler, name='confirm_project_handler'),
]