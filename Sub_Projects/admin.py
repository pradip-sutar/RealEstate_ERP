from django.contrib import admin
from .models import *

@admin.register(ProductDetails)
class ProductDetailsAdmin(admin.ModelAdmin):
    list_display = ['code', 'segment', 'product_type', 'variant', 'layout', 'units','subproject_id']  # Customize the fields you want to display

@admin.register(RaiseCost)
class RaiseCostAdmin(admin.ModelAdmin):
    list_display = ['raise_type', 'name', 'cost_per_unit','subproject_id']  # Customize the fields you want to display

@admin.register(ProductCost)
class ProductCostAdmin(admin.ModelAdmin):
    list_display = [
        'product_type_code', 'product_type', 'variant', 'floor_lane', 
        'facing', 'build_up_area', 'carpet_area','layout', 'units','units_cost','selling_cost','subproject_id'
        ]  # Customize the fields you want to display

@admin.register(ProductInventories)
class ProductInventoriesAdmin(admin.ModelAdmin):
    list_display = [
        'product_type_code', 'product_type', 'variant', 'floor_lane', 
        'facing', 'build_up_area', 'carpet_area', 'units', 'units_number', 'subproject_id'
    ]

@admin.register(SubProductImages)
class SubProductImagesAdmin(admin.ModelAdmin):
    list_display = ['type', 'description', 'images', 'subproject_id']

@admin.register(PaymentSlab)
class PaymentSlabAdmin(admin.ModelAdmin):
    list_display = ['segment', 'milestones', 'payment_slab', 'date', 'subproject_id']