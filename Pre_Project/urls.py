from django.urls import path
from . import views


urlpatterns = [    
    path('pre_project_new_handler/', views.pre_project_new_handler, name='pre_project_new_handler'),
    path('delete_pre_project_handler/<id>/', views.delete_pre_project_handler, name='delete_pre_project_handler'),
    path('confirm_project_handler/<id>/', views.transfer_to_confirm_project, name='confirm_project_handler'),
    path('confirm_project_handler/', views.transfer_to_confirm_project, name='confirm_project_handler'),
    path('delete_confirm_project_handler/<id>/', views.delete_confirm_project_handler, name='delete_confirm_project_handler'),
    path('project_segments/', views.project_segment_list, name='project_segment_list'),
    path('project_types/', views.project_type_list, name='project_type_list'),
    path('document_types/', views.document_type_list, name='document_type_list'),

    path('approval-bodies/', views.approval_body_view, name='approval-body-list-create'),  # For listing and creating
    path('approval-bodies/<int:pk>/', views.approval_body_view, name='approval-body-detail-update-delete'),  # For retrieving, updating, and deleting
]