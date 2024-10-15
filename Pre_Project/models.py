from django.db import models
from datetime import datetime
from django.db.models import Max
from System_Admin.models import System_company_detail

class Projectsegment(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Projecttype(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Documenttype(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Approval_body(models.Model):
    name=models.CharField(max_length=100)

    def __str(self):
        return self.name


class PreProjectNew(models.Model):
    OWNERSHIP_TYPE_CHOICES = [
        ('OWN', 'Owned'),
        ('REN', 'Rented'),
    ]
    project_id = models.CharField(max_length=100, unique=True, blank=True, editable=False, primary_key=True)
    project_city = models.CharField(max_length=255)
    ownership_type = models.CharField(max_length=3, choices=OWNERSHIP_TYPE_CHOICES)
    project_segments = models.CharField(max_length=100)
    project_name = models.CharField(max_length=255)
    project_types = models.CharField(max_length=100)
    project_address=models.CharField(max_length=250)
    longitude=models.CharField(max_length=200)
    latitude=models.CharField(max_length=200)
    project_measurement=models.CharField(max_length=255)
    project_description = models.TextField()
    project_area = models.CharField(max_length=250)
    approvals = models.JSONField()  # To store multiple approval entries
    expenses = models.JSONField()  # To store multiple expense entries
    document_history = models.JSONField()  # To store multiple document history entries

    def save(self, *args, **kwargs):
        if not self.project_id:
            self.project_id = self.generate_project_id()
        super(PreProjectNew, self).save(*args, **kwargs)

    def generate_project_id(self):
        # Fetch the company name from the System_company_detail model
        company = System_company_detail.objects.first()
        if company:
            company_code = company.name[:2].upper()  # First 2 letters of the company name
        else:
            company_code = 'XX'  # Default value in case there's no company data
        # First two letters of project name
        project_code = self.project_name[:2].upper() if self.project_name else 'PR'
        # First three letters of project city
        location_code = self.project_city[:3].upper() if self.project_city else 'LOC'
        # Get current year
        current_year = datetime.now().year
        # Fetch the current max serial number for this base ID
        base_id = f"{company_code}{project_code}{location_code}{current_year}"
        last_project = PreProjectNew.objects.filter(project_id__startswith=base_id).aggregate(max_id=Max('project_id'))
        last_id = last_project['max_id']

        if last_id and len(last_id) == len(base_id) + 3:
            last_serial = int(last_id[-3:])
            new_serial = last_serial + 1
        else:
            new_serial = 1

        # Zero-pad the serial number to 3 digits
        serial_str = f"{new_serial:03d}"
        return f"{base_id}/{serial_str}"


    def __str__(self):
        return self.project_name
    




class DocumentUpload(models.Model):

    APPROVAL = 'approvals'
    HISTORY = 'history'
    AGREEMENT = 'agreement'


    DOCUMENT_TYPE_CHOICES = [
        (APPROVAL, 'Approval Document'),
        (HISTORY, 'History Document'),
        (AGREEMENT, 'Agreement Document'),
    ]


    pre_project = models.ForeignKey(PreProjectNew, related_name='uploads', on_delete=models.CASCADE)
    document = models.FileField(upload_to='uploads/')
    # approval_body = models.ForeignKey(Approval_body, on_delete=models.CASCADE, null=True)
    document_type = models.CharField(max_length=100, choices=DOCUMENT_TYPE_CHOICES,  # Use choices here
        default=APPROVAL,  # Optionally, set a default
    )  # This should exist

    


class Confirm_Project(models.Model):
    project_id = models.CharField(max_length=255)
    project_city = models.CharField(max_length=255)
    ownership_type = models.CharField(max_length=3)
    project_segments = models.JSONField()  # Store as a JSON array
    project_name = models.CharField(max_length=255)
    project_types = models.JSONField()
    project_address = models.CharField(max_length=255)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    project_measurement = models.DecimalField(max_digits=10, decimal_places=2)
    project_description = models.TextField()
    project_area = models.CharField(max_length=250)
    approvals = models.JSONField()  # JSONField for multiple approval entries
    expenses = models.JSONField()  # JSONField for multiple expense entries
    document_history = models.JSONField()  # JSONField for multiple document history entries
    uploads = models.ManyToManyField(DocumentUpload, blank=True)  # Many-to-many relationship
    
    def __str__(self):
        return self.project_name

    



