from django.contrib import admin
from .models import ProductDetail, RaiseCost, ProductCost, ProductCost_1, AmenityCost

# Admin customization for ProductDetail model
@admin.register(ProductDetail)
class ProductDetailAdmin(admin.ModelAdmin):
    list_display = (
        'code', 'segment', 'product_type', 'variant', 'layout', 'units'
    )
    search_fields = ('code', 'segment', 'product_type')
    ordering = ('code',)

# Admin customization for RaiseCost model
@admin.register(RaiseCost)
class RaiseCostAdmin(admin.ModelAdmin):
    list_display = ('raise_type', 'name', 'cost_per_unit')
    search_fields = ('raise_type', 'name')
    ordering = ('raise_type',)

# Admin customization for ProductCost model
@admin.register(ProductCost)
class ProductCostAdmin(admin.ModelAdmin):
    list_display = (
        'product_type_code', 'product_type', 'variant', 'floor_lane', 'facing',
        'build_up_area', 'carpet_area', 'layout', 'units', 'unit_costs', 'selling_costs'
    )
    search_fields = ('product_type_code', 'product_type', 'variant')
    list_filter = ('facing', 'floor_lane')
    ordering = ('product_type_code',)

# Admin customization for ProductCost_1 model
@admin.register(ProductCost_1)
class ProductCost_1Admin(admin.ModelAdmin):
    list_display = (
        'product_type_code', 'product_type', 'variant', 'floor_lane', 'facing',
        'build_up_area', 'carpet_area', 'layout', 'units', 'units_number'
    )
    search_fields = ('product_type_code', 'product_type', 'variant')
    list_filter = ('facing', 'floor_lane')
    ordering = ('product_type_code',)

# Admin customization for AmenityCost model
@admin.register(AmenityCost)
class AmenityCostAdmin(admin.ModelAdmin):
    list_display = ('type', 'description', 'images')
    search_fields = ('type', 'description')
    ordering = ('type',)
