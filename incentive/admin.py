from django.contrib import admin
from .models import *

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ['target_number', 'achievement_percentage', 'uom', 'ucm','description']
