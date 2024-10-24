from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [    


    path('pre_project_new_handler/', views.pre_project_new_handler, name='pre_project_new_handler'),
    
    path('confirm_project_handler/', views.confirm_project_handler, name='confirm_project_handler'),


    #==================== master end-points ==========================================#
        path('project_segments/', views.project_segment_list, name='project_segment_list'),
        path('project_types/', views.project_type_list, name='project_type_list'),
    path('document_types/', views.document_type_list, name='document_type_list'),

    path('approval-bodies/', views.approval_body_view, name='approval-body-list-create'),  # For listing and creating
    path('approval-bodies/<int:pk>/', views.approval_body_view, name='approval-body-detail-update-delete'),  # For retrieving, updating, and deleting
]  
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)