from django.contrib import admin
from .models import *
# Register your models here.

# from rest_framework.authtoken.models import Token

# admin.site.register(Token)

@admin.register(Admin)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','department','designation','email','mob','password','token']

@admin.register(System_company_detail)
class SystemCompanyDetailsAdmin(admin.ModelAdmin):
     list_display = ['companyid', 'name', 'alias', 'company_size', 'incorporation_no', 'incorporation_certificate', 'incorporation_date', 'PAN', 'country', 'state', 'city', 'pincode', 'address', 'registered_office_details', 'email', 'mobileno', 'whatsappno','TAX_certificate']

@admin.register(System_branch_details)
class SystemBranchDetailsAdmin(admin.ModelAdmin):
    list_display = ['branch_name', 'branch_id', 'branch_type', 'country', 'state', 'city', 'branch_email', 'branch_phone']

@admin.register(System_branch_brand)
class SystemBranchBrandAdmin(admin.ModelAdmin):
    list_display = ['brand_branch_id', 'letter_header', 'letter_footer']
    search_fields = ['branch__name']

@admin.register(System_branch_contact)
class SystemBranchContactAdmin(admin.ModelAdmin):
    list_display = ['contact_name', 'designation', 'role', 'contact_email', 'contact_phone', 'contact_phone', 'contact_branch_id']
    search_fields = ['contact_name', 'designation', 'role', 'contact_email', 'branch__name']
    list_filter = ['contact_branch_id']

@admin.register(System_brand_detail)
class SystemBrandDetailAdmin(admin.ModelAdmin):
    list_display = ['company_id', 'brand_logo', 'favicon', 'letter_header', 'letter_footer']

@admin.register(System_business_detail)
class SystemBusinessDetailsAdmin(admin.ModelAdmin):
    list_display = ['company_id', 'address']

@admin.register(System_branch_type)
class SystemBranchTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_name']

@admin.register(System_contact_detail)
class SystemContactDetailsAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'role', 'email', 'mobileno', 'whatsapp', 'company_id']

@admin.register(System_social_detail)
class SystemSocialDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'Email','contact','icon']

@admin.register(System_other_detail)
class SystemOtherDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc','company_id']

@admin.register(System_bank_details)
class SystemBankDetailsAdmin(admin.ModelAdmin):
    list_display = ['bank_name', 'branch_name', 'IFSC', 'account_name', 'account_no', 'account_type','bank_logo']
    search_fields = ['bank_name', 'branch_name', 'IFSC', 'account_name', 'account_no']
    list_filter = ['account_type']




# @admin.register(Team_management)
# class TeamManagementAdmin(admin.ModelAdmin):
#     list_display = ['team_leader', 'team_member', 'department_id']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'phone', 'email', 'present_city', 'present_district',
        'present_country', 'present_pincode', 'permanent_city',
        'permanent_district', 'permanent_country', 'permanent_pincode',
        'age', 'gender', 'nationality', 'religion', 'caste'
    ]


























