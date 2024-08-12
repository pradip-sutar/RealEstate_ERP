from django.urls import path
from .views import module_handler

urlpatterns = [
    path('module_handler/', module_handler, name='module_handler'),
]
