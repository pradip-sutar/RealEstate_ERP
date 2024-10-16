from django.db import models
from Projects.models import *
from Pre_Project.models import *
from subproject_product.models import *


class Enquiry(models.Model):
    date=models.DateField()
    enquiry_id=models.CharField(max_length=100, primary_key=True)
    customer_name=models.CharField(max_length=255)
    mobile_no=models.IntegerField()
    email_id=models.EmailField(blank=True, null=True)
    city=models.CharField(max_length=255)
    project=models.ForeignKey(Confirm_Project, on_delete=models.CASCADE)
    status=models.CharField(max_length=100, choices=[
        ('Not Initiated', 'Not Initiated'), ('Initiated', 'Initiated')], default='Not Initiated')
    schedule = models.DateField(blank=True, null=True)
    stage = models.CharField(max_length=20)
    mode = models.CharField(max_length=20)
    lead_status = models.CharField(max_length=20)
    rating = models.CharField(max_length=20, blank=True)
    conversion=models.CharField(max_length=255)
    source = models.TextField(blank=True)
    mode_of_communication = models.CharField(max_length=20)
    visit = models.CharField(max_length=255)
    qoute = models.CharField(max_length=255)
    product=models.ForeignKey(Project_Product, on_delete=models.CASCADE)
 

    def __str__(self):
        return self.enquiry_id
    

class Quotation(models.Model):
    customer_id = models.ForeignKey(Enquiry, on_delete=models.CASCADE)
    enquiry_id = models.CharField(max_length=20)
    quote_id = models.CharField(max_length=20)
    version = models.DecimalField(max_digits=5, decimal_places=3)
    date = models.DateField()
    stage = models.CharField(max_length=20)
    project = models.ForeignKey(Confirm_Project, on_delete=models.CASCADE)
    products = models.ForeignKey(Project_Product, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    quotation = models.TextField(blank=True)
    follow_up_status = models.CharField(max_length=20, blank=True)
    mode = models.CharField(max_length=20)
    created_by = models.CharField(max_length=20)

    def __str__(self):
        return self.quote_id
    
class Visit(models.Model):
    customer_id = models.ForeignKey(Enquiry, on_delete=models.CASCADE, related_name='visits')
    enquiry_id = models.CharField(max_length=20)
    quote_id = models.CharField(max_length=20, primary_key=True)
    version = models.DecimalField(max_digits=5, decimal_places=3)
    date = models.DateField()
    stage = models.CharField(max_length=20)
    project = models.ForeignKey(Confirm_Project, on_delete=models.CASCADE)
    products = models.ForeignKey(Project_Product, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    visit = models.CharField(max_length=255, blank=True)
    follow_up_status = models.CharField(max_length=20, blank=True)
    mode = models.CharField(max_length=20)
    created_by = models.CharField(max_length=20)

    def __str__(self):
        return self.customer_id


class Site_visit_schedule(models.Model):
    visit_id=models.CharField(max_length=255)
    project_name = models.ForeignKey(Confirm_Project, on_delete=models.CASCADE)
    date_time = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    visit_number = models.CharField(max_length=255)
    site_manager = models.CharField(max_length=255)
    visitors=models.JSONField()
    date = models.DateField()
    time = models.TimeField()
    field_employee_name = models.CharField(max_length=255)
    sub_projects = models.ForeignKey(Project_subproject_details, on_delete=models.CASCADE)
    property = models.CharField(max_length=255)
    report = models.CharField(max_length=255)