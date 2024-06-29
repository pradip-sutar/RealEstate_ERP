from django.contrib import admin
from Employee_Management.models import *
# Register your models here.

@admin.register(Company_profile)
class EmpCompanyProfileAdmin(admin.ModelAdmin):
    list_display = ['empid', 'name', 'mobileno', 'whatsapp', 'email', 'emergency_no',
                    'date_of_joining', 'date_of_leaving', 'branch', 'department',
                    'designation', 'level', 'grade', 'role'
                    ]

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['emp_id', 'present_add', 'present_country', 'present_state',
                    'present_city', 'present_pincode', 'permanent_add', 'permanent_pincode',
                    'permanent_city', 'permanent_state', 'permanent_country'
                    ]

@admin.register(Personal_Profile)
class EmployeePersonalProfileAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'gender', 'nationality', 'DOB', 'marital_status', 'anniversary_date', 'religion', 'blood_group', 'any_medical_issues']
    search_fields = ['employee_id__username', 'nationality', 'religion', 'blood_group']
    list_filter = ['gender', 'marital_status', 'blood_group']