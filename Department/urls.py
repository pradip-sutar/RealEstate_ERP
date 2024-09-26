from django.contrib import admin
from django.urls import path, include
from Department import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('department_name_handler/', views.department_name_handler, name='department_handler'),
    path('department_designation_handler/', views.department_designation_handler, name='department_designation_handler '),
    path('department_label_handler/', views.department_label_handler, name='department_label_handler'),
    path('department_grade_handler/', views.department_grade_handler, name='department_grade_handler'),
    path('department_role_handler/', views.department_role_handler, name='department_role_handler'),
    path('designation_rights_handler/', views.designation_rights_handler, name='designation_rights_handler'),
    path('dept-doc-rights/', views.department_doc_right, name='department_doc_rights')


]   

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)