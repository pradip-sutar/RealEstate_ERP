from django.urls import path
from .views import employee_management_handler

urlpatterns = [
    path('employee_management_handler/', employee_management_handler, name='employee_management_handler'),
]
