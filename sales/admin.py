from django.contrib import admin
from .models import PaymentReceipt, PaymentSchedule, SalesAgreement

@admin.register(PaymentReceipt)
class PaymentReceiptAdmin(admin.ModelAdmin):
    list_display = ['payment_receipt_number', 'project', 'total_amount', 'received_amount', 'balance_amount']
    search_fields = ['payment_receipt_number', 'project', 'customer_id']
    list_filter = ['Date', 'mode_of_payment']

@admin.register(PaymentSchedule)
class PaymentScheduleAdmin(admin.ModelAdmin):
    list_display = ['sales_id', 'instalment_stage', 'Amount', 'payment_received']
    search_fields = ['sales_id', 'project']
    list_filter = ['date', 'payment_received']

@admin.register(SalesAgreement)
class SalesAgreementAdmin(admin.ModelAdmin):
    list_display = ['Agreement_id', 'sales_id', 'Date', 'created_by']
    search_fields = ['Agreement_id', 'sales_id', 'created_by']
    list_filter = ['Date']
