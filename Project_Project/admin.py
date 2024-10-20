from django.contrib import admin
from .models import *

@admin.register(Project_subproject_details)
class SubprojectDetailsAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'segment', 'layout', 'confirm_project_id']
    
# Register Commission model
@admin.register(Project_Commission)
class CommissionAdmin(admin.ModelAdmin):
    list_display = ['code', 'segment', 'product_type', 'variant', 'commission','confirm_project_id']

# Register PaymentSlab model
@admin.register(Project_PaymentSlab)
class PaymentSlabAdmin(admin.ModelAdmin):
    list_display = ['code', 'segment', 'milestone', 'payment_slab','confirm_project_id']


@admin.register(Project_Tax)
class ProjectTaxAdmin(admin.ModelAdmin):
    list_display = ['code', 'segment', 'product_type', 'variant', 'tax','confirm_project_id']

# Amenity Admin
@admin.register(Project_Amenity)
class ProjectAmenityAdmin(admin.ModelAdmin):
    list_display = ['code', 'amenity', 'amenity_type', 'category','confirm_project_id']

# Paid Amenity Admin
@admin.register(Project_PaidAmenity)
class ProjectPaidAmenityAdmin(admin.ModelAdmin):
    list_display = ['code', 'amenity', 'amount', 'category','confirm_project_id']

@admin.register(NearBy)
class NearByAdmin(admin.ModelAdmin):
    list_display = ['type', 'name', 'distance', 'map_url', 'confirm_project']

@admin.register(ProjectSpecification)
class ProjectSpecificationAdmin(admin.ModelAdmin):
    list_display = ['type', 'description', 'confirm_project']

@admin.register(ProjectImages)
class ProjectImagesAdmin(admin.ModelAdmin):
    list_display = ['type', 'description', 'images', 'confirm_project']




# Admin customization for ProductDetail model
# @admin.register(ProductDetail)
# class ProductDetailAdmin(admin.ModelAdmin):
#     list_display = (
#         'code', 'segment', 'product_type', 'variant', 'layout', 'units'
#     )
#     search_fields = ('code', 'segment', 'product_type')
#     ordering = ('code',)

# # Admin customization for RaiseCost model
# @admin.register(RaiseCost)
# class RaiseCostAdmin(admin.ModelAdmin):
#     list_display = ('raise_type', 'name', 'cost_per_unit')
#     search_fields = ('raise_type', 'name')
#     ordering = ('raise_type',)

# # Admin customization for ProductCost model
# @admin.register(ProductCost)
# class ProductCostAdmin(admin.ModelAdmin):
#     list_display = (
#         'product_type_code', 'product_type', 'variant', 'floor_lane', 'facing',
#         'build_up_area', 'carpet_area', 'layout', 'units', 'unit_costs', 'selling_costs'
#     )
#     search_fields = ('product_type_code', 'product_type', 'variant')
#     list_filter = ('facing', 'floor_lane')
#     ordering = ('product_type_code',)

# # Admin customization for ProductCost_1 model
# @admin.register(ProductCost_1)
# class ProductCost_1Admin(admin.ModelAdmin):
#     list_display = (
#         'product_type_code', 'product_type', 'variant', 'floor_lane', 'facing',
#         'build_up_area', 'carpet_area', 'layout', 'units', 'units_number'
#     )
#     search_fields = ('product_type_code', 'product_type', 'variant')
#     list_filter = ('facing', 'floor_lane')
#     ordering = ('product_type_code',)

# # Admin customization for AmenityCost model
# @admin.register(AmenityCost)
# class AmenityCostAdmin(admin.ModelAdmin):
#     list_display = ('type', 'description', 'images')
#     search_fields = ('type', 'description')
#     ordering = ('type',)
