from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Admin)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','department','designation','email','mob','password','token']

@admin.register(System_company_detail)
class SystemCompanyDetailsAdmin(admin.ModelAdmin):
     list_display = ['companyid', 'name', 'alias', 'company_type', 'company_size', 'incorporation_no', 'incorporation_agency', 'date', 'PAN', 'country', 'state', 'city', 'pincode', 'address', 'registered_office_details', 'email', 'mobileno', 'whatsappno','certificate','TAX_certificate']

@admin.register(System_brand_detail)
class SystemBrandDetailsAdmin(admin.ModelAdmin):
    list_display = ['company_id', 'brand_logo', 'favicon', 'letter_header', 'letter_footer']

@admin.register(System_business_detail)
class SystemBusinessDetailsAdmin(admin.ModelAdmin):
    list_display = ['company_id', 'address']

@admin.register(System_contact_detail)
class SystemContactDetailsAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'role', 'email', 'mobileno', 'whatsapp', 'company_id']

@admin.register(System_social_detail)
class SystemSocialDetailsAdmin(admin.ModelAdmin):
    list_display = ['name', 'URL', 'icon', 'company_id']

@admin.register(System_other_detail)
class SystemOtherDetailsAdmin(admin.ModelAdmin):
    list_display = ['name', 'details', 'company_id']

@admin.register(System_bank_details)
class SystemBankDetailsAdmin(admin.ModelAdmin):
    list_display = ['bank_name', 'branch_name', 'IFSC', 'account_name', 'account_no', 'account_type','bank_logo']
    search_fields = ['bank_name', 'branch_name', 'IFSC', 'account_name', 'account_no']
    list_filter = ['account_type']

@admin.register(Department_Name)
class Department_Name(admin.ModelAdmin):
    list_display = ['departmentid', 'name', 'status']

@admin.register(Department_Designation)
class Department_Designation(admin.ModelAdmin):
    list_display = ['designation', 'dept_name', 'roles_rights']

@admin.register(Department_Label)
class Department_Label(admin.ModelAdmin):
    list_display = ['designation', 'label_description', 'status']

@admin.register(Department_Grade)
class Department_Grade(admin.ModelAdmin):
    list_display = ['label', 'grade_description', 'status']


@admin.register(Team_management)
class TeamManagementAdmin(admin.ModelAdmin):
    list_display = ['team_leader', 'team_member', 'department_id']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'phone', 'email', 'present_city', 'present_district',
        'present_country', 'present_pincode', 'permanent_city',
        'permanent_district', 'permanent_country', 'permanent_pincode',
        'age', 'gender', 'nationality', 'religion', 'caste'
    ]

@admin.register(PreProjectNew)
class PreProjectNewAdmin(admin.ModelAdmin):
    list_display = [
        'project_name','project_location','ownership_type',
        'project_segment','project_type','project_area','project_description',
        'approvals','expenses','document_history','generate_agreement','upload_document'
    ]
























