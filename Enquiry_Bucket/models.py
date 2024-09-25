from django.db import models

# Create your models here.

class Quotation_Type(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Visit_Type(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Communication_Type(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Source_Type(models.Model):
    name = models.CharField(max_length=255)
    comm_type = models.ForeignKey(Communication_Type, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Enquiry_Type(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Lead_Enquiry_Stage(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Lead_Enquiry_Status(models.Model):
    lead_status = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.lead_status
    
class Lead_Activity_Status(models.Model):
    lead_status = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.lead_status