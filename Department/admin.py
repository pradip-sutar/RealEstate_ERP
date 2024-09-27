from django.contrib import admin
from . models import *

# Register your models here.
@admin.register(Department_Name)
class Department_Name(admin.ModelAdmin):
    list_display = ['id', 'name', 'status']

@admin.register(Department_Designation)
class Department_Designation(admin.ModelAdmin):
    list_display = ['designation', 'dept_name', 'status']

@admin.register(Department_Grade)
class Department_Grade(admin.ModelAdmin):
    list_display = ['level', 'grade_description']

@admin.register(Department_Roles_Rights)
class DepartmentRolesRightsAdmin(admin.ModelAdmin):
    list_display = ['id', 'role_id','role_name','view', 'write', 'edit', 'delete','department_id']