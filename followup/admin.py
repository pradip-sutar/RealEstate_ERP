from django.contrib import admin
from .models import *

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = [
        'date', 'enquiry_id', 'customer_name', 'mobile_no', 
        'email_id', 'city', 'project', 'status', 'schedule', 
        'stage', 'mode', 'lead_status', 'rating', 
        'conversion', 'source', 'mode_of_communication', 
        'visit', 'qoute', 'product'
    ]
    search_fields = ['enquiry_id', 'customer_name', 'mobile_no', 'email_id']
    list_filter = ['status', 'project', 'city']
    ordering = ['date']

@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    list_display = [
        'customer_id', 'enquiry_id', 'quote_id', 'version', 
        'date', 'stage', 'project', 'products', 'value', 
        'quotation', 'follow_up_status', 'mode', 'created_by'
    ]
    search_fields = ['quote_id', 'customer_id__enquiry_id']
    list_filter = ['stage', 'project']
    ordering = ['date']

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = [
        'customer_id', 'enquiry_id', 'quote_id', 'version', 
        'date', 'stage', 'project', 'products', 'value', 
        'visit', 'follow_up_status', 'mode', 'created_by'
    ]
    search_fields = ['quote_id', 'customer_id__enquiry_id']
    list_filter = ['stage', 'project']
    ordering = ['date']

@admin.register(Site_visit_schedule)
class SiteVisitScheduleAdmin(admin.ModelAdmin):
    list_display = [
        'visit_id', 'project_name', 'date_time', 'location', 
        'purpose', 'visit_number', 'site_manager', 
        'visitors', 'date', 'time', 'field_employee_name', 
        'sub_projects', 'property', 'report'
    ]
    search_fields = ['visit_id', 'project_name__name', 'location']
    list_filter = ['project_name', 'date']
    ordering = ['date_time']

