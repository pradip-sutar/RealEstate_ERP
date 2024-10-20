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
    measurement_unit=models.CharField(max_length=255)
    project_description = models.TextField()
    project_area = models.CharField(max_length=250)
    expenses = models.JSONField()  # To store multiple expense entries

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
        return f"{base_id}-{serial_str}"


    def __str__(self):
        return self.project_name

class Approval(models.Model):
    approvalBody = models.CharField(max_length=100)
    applyDate = models.DateField()
    employeeName = models.CharField(max_length=100)
    agency = models.CharField(max_length=100)
    approvalDate = models.DateField()
    validityNo = models.BigIntegerField()
    document = models.FileField(upload_to='approval_document/', null=True, blank=True)
    preproject = models.ForeignKey(PreProjectNew,on_delete=models.CASCADE)

class Document_History(models.Model):
    documentType = models.CharField(max_length=100)
    documentNo = models.BigIntegerField()
    issuedBy = models.CharField(max_length=100)
    issueDate = models.DateField()
    validation = models.CharField(max_length=100)
    uploadDocument = models.FileField(upload_to='document_history/', null=True, blank=True)
    preproject = models.ForeignKey(PreProjectNew,on_delete=models.CASCADE)

class Agreement(models.Model):
    upload_document = models.FileField(upload_to='agreements/', null=True, blank=True)
    preproject = models.ForeignKey(PreProjectNew,on_delete=models.CASCADE)

    


class Confirm_Project(models.Model):
    project_id = models.CharField(max_length=100, unique=True, primary_key=True)
    project_city = models.CharField(max_length=255)
    ownership_type = models.CharField(max_length=10)
    project_segments = models.CharField(max_length=100)
    project_name = models.CharField(max_length=255)
    project_types = models.CharField(max_length=100)
    project_address=models.CharField(max_length=250)
    longitude=models.CharField(max_length=200)
    latitude=models.CharField(max_length=200)
    project_measurement=models.CharField(max_length=255)
    measurement_unit=models.CharField(max_length=255)
    project_description = models.TextField()
    project_area = models.CharField(max_length=250)
    expenses = models.JSONField()
    
    def __str__(self):
        return self.project_name

class Confirm_Approval(models.Model):
    approvalBody = models.CharField(max_length=100)
    applyDate = models.DateField()
    employeeName = models.CharField(max_length=100)
    agency = models.CharField(max_length=100)
    approvalDate = models.DateField()
    validityNo = models.BigIntegerField()
    document = models.FileField(upload_to='confirm_approval_document/', null=True, blank=True)
    preproject = models.ForeignKey(Confirm_Project,on_delete=models.CASCADE)

class Confirm_Document_History(models.Model):
    documentType = models.CharField(max_length=100)
    documentNo = models.BigIntegerField()
    issuedBy = models.CharField(max_length=100)
    issueDate = models.DateField()
    validation = models.CharField(max_length=100)
    uploadDocument = models.FileField(upload_to='confirm_document_history/', null=True, blank=True)
    preproject = models.ForeignKey(Confirm_Project,on_delete=models.CASCADE)

class Confirm_Agreement(models.Model):
    upload_document = models.FileField(upload_to='confirm_agreements/', null=True, blank=True)
    preproject = models.ForeignKey(Confirm_Project,on_delete=models.CASCADE)

    



