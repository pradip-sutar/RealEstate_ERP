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

class Customer_Form(models.Model):
    name = models.CharField(max_length=255)
    mob = models.CharField(max_length=15)
    email = models.EmailField()
    present_address = models.TextField()
    present_city = models.CharField(max_length=255)
    present_district = models.CharField(max_length=255)
    present_country = models.CharField(max_length=255)
    present_pincode = models.CharField(max_length=10)
    permanent_address = models.TextField()
    permanent_city = models.CharField(max_length=255)
    permanent_district = models.CharField(max_length=255)
    permanent_country = models.CharField(max_length=255)
    permanent_pincode = models.CharField(max_length=10)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    nationality = models.CharField(max_length=255)
    religion = models.CharField(max_length=255)
    caste = models.CharField(max_length=255)

    def __str__(self):
        return self.name