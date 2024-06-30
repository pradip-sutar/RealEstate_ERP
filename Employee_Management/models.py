from django.db import models
from app1.models import Department_Name

# Create your models here.
class Company_profile(models.Model):
    empid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    mobileno = models.IntegerField()
    whatsapp = models.IntegerField(blank=True, null=True)
    email = models.EmailField()
    emergency_no = models.IntegerField()
    date_of_joining = models.DateField()
    date_of_leaving = models.DateField(blank=True, null=True)
    branch = models.CharField(max_length=255)
    department = models.ForeignKey(Department_Name, on_delete=models.CASCADE)
    designation = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Address(models.Model):
    present_add = models.TextField()
    present_country = models.CharField(max_length=255)
    present_state = models.CharField(max_length=255)
    present_city = models.CharField(max_length=255)
    present_pincode = models.CharField(max_length=20)
    permanent_add = models.TextField()
    permanent_pincode = models.CharField(max_length=20)
    permanent_city = models.CharField(max_length=255)
    permanent_state = models.CharField(max_length=255)
    permanent_country = models.CharField(max_length=255)
    employee_id = models.ForeignKey(Company_profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"Address for {self.employee_id.name}"
    
class Personal_Profile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    MARITAL_STATUS_CHOICES = [
        ('S', 'Single'),
        ('M', 'Married'),
        ('D', 'Divorced'),
        ('W', 'Widowed'),
    ]
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    nationality = models.CharField(max_length=50)
    DOB = models.DateField()
    marital_status = models.CharField(max_length=1, choices=MARITAL_STATUS_CHOICES)
    anniversary_date = models.DateField(null=True, blank=True)
    religion = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    any_medical_issues = models.TextField(null=True, blank=True)
    employee_id = models.ForeignKey(Company_profile, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.employee_id.name} - {self.nationality}"
    
class FamilyProfile(models.Model):
    details = models.JSONField()
    employee_id = models.ForeignKey(Company_profile, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.details}"
    
class EducationProfile(models.Model):
    details = models.JSONField()
    employee_id = models.ForeignKey(Company_profile, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.details}"
    
class Trainig(models.Model):
    details = models.JSONField()
    employee_id = models.ForeignKey(Company_profile, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.details}"
    
class Experience(models.Model):
    details = models.JSONField()
    employee_id = models.ForeignKey(Company_profile, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.details}"
    
class Skill_Level(models.Model):
    details = models.CharField(max_length=100)
    employee_id = models.ForeignKey(Company_profile, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.details}"
