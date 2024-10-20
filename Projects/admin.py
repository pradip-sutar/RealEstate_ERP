from django.contrib import admin
from .models import *

@admin.register(Project_Type)
class ProjectTypeAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Project_Payment_Schedule)
class ProjectPaymentScheduleAdmin(admin.ModelAdmin):
    list_display = ['id','stages', 'percentage', 'date']

@admin.register(Project_Product_Type)
class ProjectProductTypeAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Project_RaiseCost_Type)
class ProjectRaiseCostTypeAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Project_Amenity_Master)
class ProjectAmenityMasterAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Project_Nearby_Segment)
class ProjectNearbySegmentAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Project_Facing_Master)
class ProjectFacingMasterAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Project_Commission)
class ProjectCommissionAdmin(admin.ModelAdmin):
    list_display = ['id','product_type', 'commission']

@admin.register(Product_Ownership)
class ProductOwnershipAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Product_ApprovalBody)
class ProductApprovalBodyAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'status']

@admin.register(Project_Tax)
class ProjectTaxAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'amount', 'description', 'status']

# @admin.register(Project_Product)
# class ProjectProductAdmin(admin.ModelAdmin):
#     list_display = ['id','name', 'location', 'segment', 'type', 'variance', 'nos', 'area', 'cost', 'amenity']

# @admin.register(Project_add_Payment)
# class ProjectAddPaymentAdmin(admin.ModelAdmin):
#     list_display = ['id','title', 'value', 'description','confirm_project_id']

# @admin.register(Project_add_Amenity)
# class ProjectAddAmenityAdmin(admin.ModelAdmin):
#     list_display = ['id','title', 'description', 'image']

# @admin.register(Project_add_Commission)
# class ProjectAddAmenityAdmin(admin.ModelAdmin):
#     list_display = ['id','commission', 'amount', 'confirm_project_id']

# @admin.register(Project_add_Tax)
# class ProjectAddTaxAdmin(admin.ModelAdmin):
#     list_display = ['name', 'tax_amount', 'confirm_project_id']
#     search_fields = ['name', 'confirm_project_id__name']
#     list_filter = ['confirm_project_id']

# @admin.register(Project_add_PaidAmenity)
# class ProjectAddPaidAmenityAdmin(admin.ModelAdmin):
#     list_display = ['title', 'cost', 'confirm_project_id']
#     search_fields = ['title', 'confirm_project_id__name']
#     list_filter = ['confirm_project_id']

# @admin.register(Project_add_Price)
# class ProjectAddPriceAdmin(admin.ModelAdmin):
#     list_display = ['name', 'purchase', 'base', 'market', 'total', 'confirm_project_id']
#     search_fields = ['name', 'purchase', 'confirm_project_id__name']
#     list_filter = ['confirm_project_id']

# @admin.register(Project_add_Inventory)
# class ProjectAddInventoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'category', 'quantity', 'build', 'total', 'carpet', 'sold', 'available', 'confirm_project_id']
#     search_fields = ['name', 'category', 'confirm_project_id__name']
#     list_filter = ['confirm_project_id']

