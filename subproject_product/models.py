# models.py
from django.db import models

class ProductSpecification(models.Model):
    product_code = models.CharField(max_length=255)
    product_name=models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_specifications/', blank=True, null=True)
    specification = models.CharField(max_length=255)
    size = models.CharField(max_length=100)
    direction = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.product_code} - {self.specification}"

class ProductImage(models.Model):
    type = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.type} - {self.description}"


class EnquirySummary(models.Model):
    date = models.DateField()
    enquiry_type = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    agent = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)
    associate = models.CharField(max_length=100)

    def __str__(self):
        return f"Enquiry {self.enquiry_type} - {self.product_type}"

class VisitSummary(models.Model):
    date = models.DateField()
    enquiry_type = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    agent = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)
    associate = models.CharField(max_length=100)

    def __str__(self):
        return f"Visit {self.enquiry_type} - {self.product_type}"

class QuoteSummary(models.Model):
    date = models.DateField()
    enquiry_type = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    agent = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)
    associate = models.CharField(max_length=100)

    def __str__(self):
        return f"Quote {self.enquiry_type} - {self.product_type}"

class EmployeeStatus(models.Model):
    enquiry_type = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    agent = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)
    associate = models.CharField(max_length=100)

    def __str__(self):
        return f"Employee {self.enquiry_type} - {self.product_type}"

class CustomerInformation(models.Model):
    enquiry_type = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    agent = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)
    associate = models.CharField(max_length=100)

    def __str__(self):
        return f"Customer {self.enquiry_type} - {self.product_type}"

class CommissionDetails(models.Model):
    total_commission = models.DecimalField(max_digits=10, decimal_places=2)
    agent = models.CharField(max_length=100)
    commission_type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    associate = models.CharField(max_length=100)
    commission_status = models.CharField(max_length=100)

    def __str__(self):
        return f"Commission {self.agent} - {self.commission_type}"

class PaymentDetails(models.Model):
    total_payment = models.DecimalField(max_digits=10, decimal_places=2)
    agent = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    invoice = models.CharField(max_length=100)

    def __str__(self):
        return f"Payment {self.agent} - {self.payment_status}"

class CustomerDocument(models.Model):
    date = models.DateField()
    document_for = models.CharField(max_length=100)
    document_type = models.CharField(max_length=100)
    image = models.ImageField(upload_to='customer_documents/')
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"Document {self.document_for} - {self.document_type}"

class PropertyDocument(models.Model):
    date = models.DateField()
    document_for = models.CharField(max_length=100)
    document_type = models.CharField(max_length=100)
    image = models.ImageField(upload_to='property_documents/')
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"Property Document {self.document_for} - {self.document_type}"
