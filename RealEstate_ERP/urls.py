from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/<int:mob>/', views.admin_view),
    path('admin-login/', views.admin_login),
    path('department_name_handler/', views.department_name_handler, name='create_department'),
    path('department_name_handler/<int:departmentid>/', views.department_name_handler, name='get_department'),
    path('department_label_handler/', views.department_label_handler, name='create_label'),
    path('department_label_handler/<int:labelid>/', views.department_label_handler, name='get_label'),
    path('department_grade_handler/', views.department_grade_handler, name='create_grade'),
    path('department_grade_handler/<int:gradeid>/', views.department_grade_handler, name='get_grade'),
    path('department_designation_handler/', views.department_designation_handler, name='create_designation'),
    path('department_designation_handler/<int:designationid>/', views.department_designation_handler, name='get_designation'),
    path('system_company_type_handler/', views.system_company_type_handler, name='create_system_company_type_handler'),
    path('system_company_type_handler/<str:type_name>/', views.system_company_type_handler, name='get_system_company_type_handler'),
    path('system_company_details_handler/', views.system_company_details_handler, name='create_system_company_details_handler'),
    path('system_company_details_handler/<int:id>/', views.system_company_details_handler, name='get_system_company_details_handler'),
    path('system_company_brand_handler/', views.system_company_brand_handler, name='create_system_company_brand_handler'),
    path('system_company_brand_handler/<int:id>/', views.system_company_brand_handler, name='get_system_company_brand_handler'),
    path('system_company_business_details/', views.system_business_details_handler, name='system_business_details_handler'),
    path('system_contact_details_handler/', views.system_contact_details_handler, name='system_contact_details_handler'),
    path('system_social_details_handler/', views.system_social_details_handler, name='system_social_details_handler'),
    path('system_other_details_handler/', views.system_other_details_handler, name='system_other_details_handler'),
    path('system_branch_type_handler/', views.system_branch_type_handler, name='system_branch_type_handler'),
    path('system_branch_details_handler/', views.system_branch_details_handler, name='system_branch_details_handler'),
    path('system_branch_brand_handler/', views.system_branch_brand_handler, name='system_branch_brand_handler'),
    path('system_branch_contact_handler/', views.system_branch_contact_handler, name='system_branch_contact_handler'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)