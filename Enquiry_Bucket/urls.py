from django.urls import path
from . import views

urlpatterns = [
    path('quotation_types_handler/', views.quotation_type_handler, name='quotation_types_handler'),
    path('visit_type_handler/', views.visit_type_handler),
    path('communication_type_handler/', views.communication_type_handler),
    path('source_type_handler/', views.source_type_handler),
    path('enquiry_type_handler/', views.enquiry_type_handler),
    path('lead_enquiry_stage_handler/', views.lead_enquiry_stage_handler),
    path('lead_enquiry_status_handler/', views.lead_enquiry_status_handler),
    path('lead_activity_status_handler/', views.lead_activity_status_handler)
]
