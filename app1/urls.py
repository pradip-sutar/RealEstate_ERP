from django.contrib import admin
from django.urls import path, include
from app1 import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('user/<int:mob>/', views.admin_view),
    path('admin-login/', views.admin_login),
    path('system_company_details_handler/', views.system_company_details_handler, name='create_system_company_details_handler'),
    path('system_company_details_handler/<int:id>/', views.system_company_details_handler, name='get_system_company_details_handler'),
    path('system_company_brand_handler/', views.system_company_brand_handler, name='create_system_company_brand_handler'),
    path('system_company_brand_handler/<int:id>/', views.system_company_brand_handler, name='get_system_company_brand_handler'),
    path('system_company_business_details/', views.system_business_details_handler, name='system_business_details_handler'),
    path('system_contact_details_handler/', views.system_contact_details_handler, name='system_contact_details_handler'),
    path('system_social_details_handler/', views.system_social_details_handler, name='system_social_details_handler'),
    path('system_other_details_handler/', views.system_other_details_handler, name='system_other_details_handler'),
    path('system_branch_type_handler/', views.system_branch_type_handler, name='system_branch_type_handler'),
    path('system_branch_handler/', views.system_branch_handler, name='system_branch_handler'),
    path('system_bank_details_handler/', views.system_bank_details_handler, name='system_bank_details_handler'),
    path('system_board_of_directors_handler/', views.system_board_of_directors_handler, name='board_of_directors_handler'),
    path('customer_handler/', views.customer_handler, name='customer_handler'),
    path('department_name_handler/', views.department_name_handler, name='department_handler'),
    path('department_designation_handler/', views.department_designation_handler, name='department_designation_handler '),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)