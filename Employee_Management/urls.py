from django.urls import path
from .views import *

urlpatterns = [
    path('employee_management_handler/', employee_management_handler, name='employee_management_handler'),
    path('employee_bank_handler/', bank_others_view, name='bank_others_view'),
]
