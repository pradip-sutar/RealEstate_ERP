from django.contrib import admin
from . models import *

# Register your models here.
@admin.register(Department_Name)
class Department_Name(admin.ModelAdmin):
    list_display = ['id', 'name', 'status']

@admin.register(Department_Designation)
class Department_Designation(admin.ModelAdmin):
    list_display = ['designation', 'dept_name', 'roles_rights']

@admin.register(Department_Label)
class Department_Label(admin.ModelAdmin):
    list_display = ['designation', 'label_description', 'status']

@admin.register(Department_Grade)
class Department_Grade(admin.ModelAdmin):
    list_display = ['label', 'grade_description', 'status']