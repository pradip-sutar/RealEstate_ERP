from django.contrib import admin
from .models import *

@admin.register(PreProjectNew)
class PreProjectNewAdmin(admin.ModelAdmin):
    list_display = (
        'project_id', 
        'project_city', 
        'ownership_type', 
        'project_segments', 
        'project_name', 
        'project_types',
        'project_address',
        'longitude',
        'latitude',
        'project_measurement',
        'project_description', 
        'project_area', 
        'expenses', 
    )

@admin.register(Approval)
class ApprovalAdmin(admin.ModelAdmin):
    list_display = ['approvalBody', 'applyDate', 'employeeName', 'agency', 'approvalDate', 'validityNo', 'document', 'preproject']

@admin.register(Document_History)
class DocumentHistoryAdmin(admin.ModelAdmin):
    list_display = ['documentType', 'documentNo', 'issuedBy', 'issueDate', 'validation', 'uploadDocument', 'preproject']

@admin.register(Agreement)
class AgreementAdmin(admin.ModelAdmin):
    list_display = ['upload_document', 'preproject']

# @admin.register(Confirm_Project)
# class ConfirmProjectAdmin(admin.ModelAdmin):
#     list_display = (
#         'project_id',
#         'project_city',
#         'ownership_type',
#         'project_segments',
#         'project_name',
#         'project_types',
#         'project_address',
#         'longitude',
#         'latitude',
#         'project_measurement',
#         'project_description',
#         'project_area',
#         'approvals',  # Custom method
#         'expenses',   # Custom method
#         'document_history'  # Custom method
#     )

   
@admin.register(Projectsegment)
class ProjectSegmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Projecttype)
class ProjectTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Documenttype)
class DocumenttypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(Approval_body)
class ApprovalBodyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

