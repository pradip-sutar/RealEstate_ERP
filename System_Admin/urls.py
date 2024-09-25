from django.contrib import admin
from django.urls import path, include
from System_Admin import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('admin_view/<int:mob>/', views.admin_view),
    path('admin_login/', views.admin_login),
    path('system_company_details_handler/', views.system_company_details_handler, name='system_company_details_handler'),
    path('system_branch_type_handler/', views.system_branch_type_handler, name='system_branch_type_handler'),
    path('system_branch_handler/', views.system_branch_handler, name='system_branch_handler'),
    path('system_bank_details_handler/', views.system_bank_details_handler, name='system_bank_details_handler'),
    path('system_board_of_directors_handler/', views.system_board_of_directors_handler, name='board_of_directors_handler'),
    path('customer_handler/', views.customer_handler, name='customer_handler'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)