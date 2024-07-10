from django.urls import path
from .views import *

urlpatterns = [
    path('employee_management_handler/', employee_management_handler, name='employee_management_handler'),
    path('employee_bank_handler/', bank_others_view, name='bank_others_view'),
    path('employee_salary_handler/', employee_salary_handler, name='employee_salary_handler'),
    path('employee_document_handler/', employee_document_handler, name='employee_document_handler'),
]
