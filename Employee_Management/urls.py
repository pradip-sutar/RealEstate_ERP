from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('employee_management_handler/', employee_data, name='employee_management'),
    path('employee_bank_handler/', bank_others_view, name='bank_others_view'),
    path('employee_salary_handler/', employee_salary_handler, name='employee_salary_handler'),
    path('employee-admin-kyc/', employee_kyc_list, name='employee_kyc_list'),
    path('employee-kyc-details/<int:employee_id>/', employee_kyc_detail, name='employee_kyc_detail'),
    path('unique-employee-name/', get_unique_employee_kyc, name='get_unique_employee_kyc'),
    path('employee-status-update/', update_status, name='update_employee_kyc_status'),      
    path('emp-doc-rights/', employee_document_rights, name='employee_document_rights'),


    path('fetch-doc-rights/', doc_rights_fetch, name='fetch_document_rights'),


    path('document-download/<str:empid>/<str:document_name>/', document_download, name='document-download'),


    path('document-master/', document_master_view, name='document-master-list'),
    path('document-master/<int:pk>/', document_master_view, name='document-detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  #this is the urls.py
