from django.contrib import admin
from .models import *

@admin.register(Quotation_Type)
class QuotationTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']


@admin.register(Visit_Type)
class VisitTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']

@admin.register(Communication_Type)
class CommunicationTypeAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Source_Type)
class SourceTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'comm_type', 'status']

@admin.register(Enquiry_Type)
class EnquiryTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']

@admin.register(Lead_Enquiry_Stage)
class LeadEnquiryStageAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']

@admin.register(Lead_Enquiry_Status)
class LeadEnquiryStatusAdmin(admin.ModelAdmin):
    list_display = ['lead_status', 'status']

@admin.register(Customer_Form)
class CustomerFormAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'mob', 'email', 'present_city', 'present_district', 'present_country', 'present_pincode',
        'permanent_city', 'permanent_district', 'permanent_country', 'permanent_pincode', 'age', 'gender',
        'nationality', 'religion', 'caste'
    ]