from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(PreProjectNew)
class PreProjectNewAdmin(admin.ModelAdmin):
    list_display = ['id',
        'project_name','project_location','ownership_type',
        'project_segment','project_type','project_area','project_description',
        'approvals','expenses','document_history','generate_agreement1','generate_agreement2','upload_document1','upload_document2'
    ]

@admin.register(Confirm_Project)
class ConfirmProjectAdmin(admin.ModelAdmin):
    list_display = ['id',
        'project_name','project_location','ownership_type',
        'project_segment','project_type','project_area','project_description',
        'approvals','expenses','document_history','generate_agreement','upload_document'
    ]