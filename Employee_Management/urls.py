from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('employee_data/', employee_data, name='employee_management'),
    path('employee_bank_handler/', bank_others_view, name='bank_others_view'),
    path('employee_salary_handler/', employee_salary_handler, name='employee_salary_handler'),
    path('employee-kyc/', employee_kyc_list, name='employee_kyc_list'),
    path('employee-kyc/<int:employee_id>/', employee_kyc_detail, name='employee_kyc_detail'),
    path('employee-kyc-name/', get_unique_employee_kyc, name='employee_kyc_detail'),
    path('employee-kyc-update/', update_status, name='employee_kyc_detail'),


    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)