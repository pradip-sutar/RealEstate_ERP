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
        'approvals', 
        'expenses', 
        'document_history', 
    )

@admin.register(Confirm_Project)
class ConfirmProjectAdmin(admin.ModelAdmin):
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
        'approvals',  # Custom method
        'expenses',   # Custom method
        'document_history'  # Custom method
    )
def project_id(self, obj):
        return obj.project_id.project_id  # Access project_id from PreProjectNew
    
project_id.short_description = 'Project ID'
   
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

@admin.register(DocumentUpload)
class DocumentUploadAdmin(admin.ModelAdmin):
    list_display = ('pre_project','document_type','document')
    search_fields = ('pre_project__project_name',)
