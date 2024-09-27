from django.contrib import admin
from .models import *

@admin.register(Customer_Form)
class CustomerFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'mob', 'email', 'present_city', 'present_district', 'present_country', 'present_pincode',
        'permanent_city', 'permanent_district', 'permanent_country', 'permanent_pincode', 'age', 'gender',
        'nationality', 'religion', 'caste']
