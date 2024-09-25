from django.contrib import admin
from .models import *

@admin.register(Roles)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Rights)
class RightsAdmin(admin.ModelAdmin):
    list_display = ['id', 'roles_id','roles_name','view', 'write', 'edit', 'delete']