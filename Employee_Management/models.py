from django.db import models
from Department.models import *
from System_Admin.models import *

# Create your models here.
class Company_profile(models.Model):
    empid = models.IntegerField(primary_key=True)
    photo= models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    name = models.CharField(max_length=255)
    mobileno = models.IntegerField()
    whatsapp = models.IntegerField(blank=True, null=True)
    email = models.EmailField()
    emergency_no = models.IntegerField()
    date_of_joining = models.CharField(max_length=100)
    date_of_leaving = models.CharField(max_length=100,blank=True, null=True)
    branch = models.CharField(max_length=255)
    department = models.ForeignKey(Department_Name, on_delete=models.CASCADE)
    designation = models.CharField(max_length=255)
    # level = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    document_rights=models.JSONField(blank=True, null=True)

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
    DOB = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=1, choices=MARITAL_STATUS_CHOICES)
    anniversary_date = models.CharField(max_length=100, blank=True, null=True)
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
    certificate=models.ImageField(upload_to='media/profile_pics/certificates', null=True, blank=True)
    marklist=models.ImageField(upload_to='media/profile_pics/certificates', null=True, blank=True)
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
    experience_letter=models.ImageField(upload_to='media/profile_pics/certificates', null=True, blank=True)
    Joining_letter=models.ImageField(upload_to='media/profile_pics/certificates', null=True, blank=True)
    employee_id = models.ForeignKey(Company_profile, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.details}"
    
class Skill_Level(models.Model):
    details = models.CharField(max_length=100)
    employee_id = models.ForeignKey(Company_profile, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.details}"




class Bank_Others(models.Model):
    bank_name = models.CharField(max_length=255)
    branch_name = models.CharField(max_length=255)
    IFSC = models.CharField(max_length=11)
    account_type = models.CharField(max_length=50)
    account_name = models.CharField(max_length=255)
    account_no = models.CharField(max_length=20)
    proof_image = models.ImageField(upload_to='bank_proof_images/')
    epfo_no = models.CharField(max_length=20, blank=True, null=True)
    epfo_state = models.CharField(max_length=255, blank=True, null=True)
    epfo_branch = models.CharField(max_length=255, blank=True, null=True)
    insurance_no = models.CharField(max_length=20, blank=True, null=True)
    insurance_provider = models.CharField(max_length=255, blank=True, null=True)
    insurance_state = models.CharField(max_length=255, blank=True, null=True)
    insurance_branch = models.CharField(max_length=255, blank=True, null=True)
    employee_id = models.ForeignKey(Company_profile,on_delete=models.CASCADE)

    def __str__(self):
        return self.bank_name
    

class Employee_Salary(models.Model):
    joining_salary = models.DecimalField(max_digits=10, decimal_places=2)
    ctc = models.DecimalField(max_digits=10, decimal_places=2)
    joining_letter = models.FileField(upload_to='joining_letters/', blank=True, null=True)
    joining_date = models.CharField(max_length=100)
    department = models.ForeignKey(Department_Name, on_delete=models.CASCADE)
    designation = models.ForeignKey(Department_Designation, on_delete=models.CASCADE)
    grade = models.ForeignKey(Department_Grade, on_delete=models.CASCADE)
    branch = models.ForeignKey(System_branch_type, on_delete=models.CASCADE)
    increment_date = models.CharField(max_length=100, blank=True, null=True)
    promotion_date = models.CharField(max_length=100, blank=True, null=True)
    increased_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    increased_ctc = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    transfer_date = models.CharField(max_length=100, blank=True, null=True)
    employee_id = models.ForeignKey(Company_profile,on_delete=models.CASCADE)

    def __str__(self):
        return f"Employee Salary ({self.department} - {self.designation})"
    


class EmployeeKYC(models.Model):

    STATUS_CHOICES = [
        ('Pending','Pending'),
        ('Completed','Completed')
    ]
    employee_id = models.ForeignKey(Company_profile, on_delete=models.CASCADE)
    document_name = models.CharField(max_length=100)
    issued_from = models.CharField(max_length=100)
    issue_date = models.DateField()
    document_number = models.CharField(max_length=50)
    validity = models.DateField()  # Renamed from 'validity'
    upload = models.FileField(upload_to='employee_documents/', blank=True, null=True)
    Status = models.CharField(max_length=10, choices=STATUS_CHOICES ,default='Pending')
    def __str__(self):
        return self.document_name

    class Meta:
        verbose_name = "Employee KYC Document"
        verbose_name_plural = "Employee KYC Documents"
        ordering = ['issue_date']



class Document_master(models.Model):
    document_name = models.CharField(max_length=100)

    def __str__(self):
        return self.document_name


