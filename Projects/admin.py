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

@admin.register(Segment)
class ProjectSegmentAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Varient)
class ProjectVarientAdmin(admin.ModelAdmin):
    list_display = ['id','name']
