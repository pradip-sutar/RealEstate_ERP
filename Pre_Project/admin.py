from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(PreProjectNew)
class PreProjectNewAdmin(admin.ModelAdmin):
    list_display = [
        'project_name','project_location','ownership_type',
        'project_segment','project_type','project_area','project_description',
        'approvals','expenses','document_history','generate_agreement','upload_document'
    ]