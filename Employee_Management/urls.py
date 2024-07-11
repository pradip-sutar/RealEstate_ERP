from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('employee_management_handler/', employee_management_handler, name='employee_management_handler'),
    path('employee_bank_handler/', bank_others_view, name='bank_others_view'),
    path('employee_salary_handler/', employee_salary_handler, name='employee_salary_handler'),
    path('employee_document_handler/', employee_document_handler, name='employee_document_handler'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)