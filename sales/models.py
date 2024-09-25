from django.db import models

class PaymentReceipt(models.Model):
    customer_id = models.CharField(max_length=255)
    enquiry_id = models.CharField(max_length=255)
    quote_id = models.CharField(max_length=255)
    sales_id = models.CharField(max_length=255)
    Date=models.DateField()
    project=models.CharField(max_length=100)
    product = models.CharField(max_length=255)
    payment_receipt_number = models.CharField(max_length=255)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    received_amount = models.DecimalField(max_digits=10, decimal_places=2)
    mode_of_payment = models.CharField(max_length=255)
    transaction_id = models.CharField(max_length=255)
    platform = models.CharField(max_length=255, blank=True)  # Optional field
    account_name = models.CharField(max_length=255, blank=True)  # Optional field
    account_number = models.CharField(max_length=255, blank=True)  # Optional field
    # Next due date
    next_pay_date = models.DateField(blank=True, null=True)  # Optional field
    balance_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Medium of payment (might be same as mode_of_payment)
    medium_of_payment = models.CharField(max_length=255)
    
    def __str__(self):
        return f"PaymentReceipt {self.payment_receipt_number} - {self.project}"

class PaymentSchedule(models.Model):
    sales_id = models.ForeignKey(PaymentReceipt, on_delete=models.CASCADE)  # Foreign key to PaymentReceipt
    project = models.CharField(max_length=255)
    date = models.DateField()
    instalment_stage = models.CharField(max_length=255)
    statement = models.CharField(max_length=255, blank=True)  # Optional field for additional details
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_received = models.BooleanField(default=False)

    def __str__(self):
        return f"PaymentSchedule {self.instalment_stage} for {self.project}"


class SalesAgreement(models.Model):  # Corrected model class name to start with capital 'S'
    sales_id = models.ForeignKey(PaymentReceipt, on_delete=models.CASCADE)  # Foreign key to PaymentReceipt
    Agreement_id = models.CharField(max_length=10)
    Date = models.DateField()
    created_by = models.CharField(max_length=50)
    Upload_by = models.CharField(max_length=50)
    upload_file = models.FileField(upload_to='SaleAgreement/', blank=True, null=True)  # Upload folder

    def __str__(self):
        return f"Sales Agreement {self.Agreement_id} - {self.sales_id}"
