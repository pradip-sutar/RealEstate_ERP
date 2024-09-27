from django.urls import path
from .views import *

urlpatterns = [
    path('roles_handler/', roles_handler, name='module_handler'),
    path('rights_handler/', rights_handler, name='rights_handler'),
]
