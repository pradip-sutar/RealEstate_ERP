from django.contrib import admin
from .models import *

@admin.register(ProductSpecification)
class ProductSpecificationAdmin(admin.ModelAdmin):
    list_display = ('product_code', 'specification', 'size', 'direction', 'image')


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('type', 'description', 'image')


@admin.register(EnquirySummary)
class EnquirySummaryAdmin(admin.ModelAdmin):
    list_display = ('date', 'enquiry_type', 'product_type', 'status', 'agent', 'activity', 'associate')


@admin.register(VisitSummary)
class VisitSummaryAdmin(admin.ModelAdmin):
    list_display = ('date', 'enquiry_type', 'product_type', 'status', 'agent', 'activity', 'associate')


@admin.register(QuoteSummary)
class QuoteSummaryAdmin(admin.ModelAdmin):
    list_display = ('date', 'enquiry_type', 'product_type', 'status', 'agent', 'activity', 'associate')


@admin.register(EmployeeStatus)
class EmployeeStatusAdmin(admin.ModelAdmin):
    list_display = ('enquiry_type', 'product_type', 'status', 'agent', 'activity', 'associate')


@admin.register(CustomerInformation)
class CustomerInformationAdmin(admin.ModelAdmin):
    list_display = ('enquiry_type', 'product_type', 'status', 'agent', 'activity', 'associate')


@admin.register(CommissionDetails)
class CommissionDetailsAdmin(admin.ModelAdmin):
    list_display = ('total_commission', 'agent', 'commission_type', 'amount', 'associate', 'commission_status')


@admin.register(PaymentDetails)
class PaymentDetailsAdmin(admin.ModelAdmin):
    list_display = ('total_payment', 'agent', 'payment_status', 'payment_method', 'invoice')


@admin.register(CustomerDocument)
class CustomerDocumentAdmin(admin.ModelAdmin):
    list_display = ('date', 'document_for', 'document_type', 'image', 'status')


@admin.register(PropertyDocument)
class PropertyDocumentAdmin(admin.ModelAdmin):
    list_display = ('date', 'document_for', 'document_type', 'image', 'status')
