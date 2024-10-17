from django.urls import path
from .views import *

urlpatterns = [
    path('enquiry/', enquiry_view, name='enquiry'),
    path('quotation/', quotation_view, name='quotation'),
    path('visit/', visit_view, name='visit'),
    path('site-visit-schedule/', site_visit_schedule_view, name='site_visit_schedule'),
]
