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



###############################################################################################

@admin.register(Confirm_Project)
class ConfirmProjectAdmin(admin.ModelAdmin):
    list_display = ('project_id', 'project_name', 'project_city', 'ownership_type', 'project_segments', 'project_types', 'project_area')
    search_fields = ('project_name', 'project_city', 'project_types', 'ownership_type')
    list_filter = ('project_city', 'ownership_type', 'project_segments', 'project_types')
    readonly_fields = ('project_id',)  # Making project_id read-only since it's not editable

@admin.register(Confirm_Approval)
class ConfirmApprovalAdmin(admin.ModelAdmin):
    list_display = ['approvalBody', 'applyDate', 'employeeName', 'agency', 'approvalDate', 'validityNo', 'preproject']
    search_fields = ('approvalBody', 'employeeName', 'agency')
    list_filter = ('approvalDate', 'applyDate')

# Registering Confirm_Document_History model
@admin.register(Confirm_Document_History)
class ConfirmDocumentHistoryAdmin(admin.ModelAdmin):
    list_display = ['documentType', 'documentNo', 'issuedBy', 'issueDate', 'validation', 'preproject']
    search_fields = ('documentType', 'issuedBy')
    list_filter = ('issueDate',)

# Registering Confirm_Agreement model
@admin.register(Confirm_Agreement)
class ConfirmAgreementAdmin(admin.ModelAdmin):
    list_display = ('upload_document', 'preproject')
    search_fields = ('upload_document',)

   
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

