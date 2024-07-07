from django.db import models

# Create your models here.
class PreProjectNew(models.Model):
    OWNERSHIP_TYPE_CHOICES = [
        ('OWN', 'Owned'),
        ('REN', 'Rented'),
    ]
    PROJECT_SEGMENT_CHOICES = [
        ('RES', 'Residential'),
        ('COM', 'Commercial'),
        ('IND', 'Industrial'),
    ]
    PROJECT_TYPE_CHOICES = [
        ('NEW', 'New Construction'),
        ('REN', 'Renovation'),
        ('EXT', 'Extension'),
    ]
    project_location = models.CharField(max_length=255)
    ownership_type = models.CharField(max_length=3, choices=OWNERSHIP_TYPE_CHOICES)
    project_segment = models.CharField(max_length=3, choices=PROJECT_SEGMENT_CHOICES)
    project_name = models.CharField(max_length=255)
    project_type = models.CharField(max_length=3, choices=PROJECT_TYPE_CHOICES)
    project_description = models.TextField()
    project_area = models.DecimalField(max_digits=10, decimal_places=2)
    approvals = models.JSONField()  # To store multiple approval entries
    expenses = models.JSONField()  # To store multiple expense entries
    document_history = models.JSONField()  # To store multiple document history entries
    generate_agreement = models.FileField(upload_to='pre_projects_agreements/',blank=True,null=True)
    upload_document = models.FileField(upload_to='pre_projects_documents/',blank=True,null=True)
    def __str__(self):
        return self.project_name
    

class Confirm_Project(models.Model):
    
    OWNERSHIP_TYPE_CHOICES = [
        ('OWN', 'Owned'),
        ('REN', 'Rented'),
    ]
    PROJECT_SEGMENT_CHOICES = [
        ('RES', 'Residential'),
        ('COM', 'Commercial'),
        ('IND', 'Industrial'),
    ]
    PROJECT_TYPE_CHOICES = [
        ('NEW', 'New Construction'),
        ('REN', 'Renovation'),
        ('EXT', 'Extension'),
    ]
    project_location = models.CharField(max_length=255)
    ownership_type = models.CharField(max_length=3, choices=OWNERSHIP_TYPE_CHOICES)
    project_segment = models.CharField(max_length=3, choices=PROJECT_SEGMENT_CHOICES)
    project_name = models.CharField(max_length=255)
    project_type = models.CharField(max_length=3, choices=PROJECT_TYPE_CHOICES)
    project_description = models.TextField()
    project_area = models.DecimalField(max_digits=10, decimal_places=2)
    approvals = models.JSONField()  # To store multiple approval entries
    expenses = models.JSONField()  # To store multiple expense entries
    document_history = models.JSONField()  # To store multiple document history entries
    generate_agreement = models.FileField(upload_to='confirm_project_agreements/',blank=True,null=True)
    upload_document = models.FileField(upload_to='confirm_projects_documents/',blank=True,null=True)
    def __str__(self):
        return self.project_name
    



