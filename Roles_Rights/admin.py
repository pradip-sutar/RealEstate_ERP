from django.contrib import admin
from .models import Roles

@admin.register(Roles)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
