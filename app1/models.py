from django.db import models

# Create your models here.
class Admin(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    mob = models.BigIntegerField(primary_key=True)
    password = models.BigIntegerField()
    email = models.EmailField()
    token = models.CharField(max_length=128)
    def __str__(self):
        return f"{self.name}"

class System_company_detail(models.Model):
    companyid = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, blank=True, null=True)
    company_size = models.CharField(max_length=255)
    incorporation_no = models.CharField(max_length=255)
    incorporation_agency = models.CharField(max_length=255)
    date = models.DateField()
    certificate = models.FileField(upload_to='company_certificates/', blank=True, null=True)
    TAX_certificate = models.FileField(upload_to='tax_certificates/', blank=True, null=True)
    PAN = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    pincode = models.CharField(max_length=20)
    address = models.TextField()
    registered_office_details = models.TextField()
    email = models.EmailField()
    mobileno = models.CharField(max_length=15)
    whatsappno = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name

class System_brand_detail(models.Model):
    brand_logo = models.ImageField(upload_to='brand_logos/', blank=True, null=True)
    favicon = models.ImageField(upload_to='favicons/', blank=True, null=True)
    letter_header = models.ImageField(upload_to='letter_headers/', blank=True, null=True)
    letter_footer = models.ImageField(upload_to='letter_footers/', blank=True, null=True)
    company_id = models.ForeignKey(System_company_detail, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.company_id.name}"

class System_business_detail(models.Model):
    address = models.TextField()
    company_id = models.ForeignKey(System_company_detail, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.company_id.name} - Business Details"

class System_contact_detail(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    email = models.EmailField()
    mobileno = models.CharField(max_length=15)
    whatsapp = models.CharField(max_length=15, blank=True, null=True)
    company_id = models.ForeignKey(System_company_detail, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.company_id.name})"

class System_social_detail(models.Model):
    details = models.JSONField()  # Changed to JSONField
    company_id = models.ForeignKey(System_company_detail, on_delete=models.CASCADE)

    def __str__(self):
        return f"Social Details ({self.company_id.name})"

class System_other_detail(models.Model):
    details = models.JSONField()  # Changed to JSONField
    company_id = models.ForeignKey(System_company_detail, on_delete=models.CASCADE)

    def __str__(self):
        return f"Other Details ({self.company_id.name})"
    
class System_branch_type(models.Model):
    type_name = models.CharField(max_length=100)
    def __str__(self):
        return self.type_name
    
class System_branch_details(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, blank=True, null=True)
    branch_id = models.BigIntegerField(primary_key=True)
    branch_type = models.ForeignKey(System_branch_type, on_delete=models.CASCADE)
    size = models.CharField(max_length=255)
    incorporation_no = models.CharField(max_length=255)
    incorporation_age = models.CharField(max_length=255)
    incorporation_date = models.DateField()
    incorporation_certificate = models.FileField(upload_to='incorporation_certificates/',blank=True,null=True)
    tax_certificate_details = models.TextField()
    PAN = models.CharField(max_length=10)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    PIN = models.CharField(max_length=20)
    address = models.TextField()
    registered_office_address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    whatsapp = models.CharField(max_length=15, blank=True, null=True)
    def __str__(self):
        return f"{self.name} ({self.branch_id})"
    
class System_branch_brand(models.Model):
    letter_header = models.FileField(upload_to='letter_headers/',null=True, blank=True)
    letter_footer = models.FileField(upload_to='letter_footers/',null=True, blank=True)
    branch = models.ForeignKey(System_branch_details, on_delete=models.CASCADE)
    def __str__(self):
        return f"Brand for Branch ID: {self.branch.branch_id}"
    
class System_branch_contact(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    whatsapp = models.CharField(max_length=15, blank=True, null=True)
    branch = models.ForeignKey(System_branch_details, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.designation} ({self.branch.name})"

class System_bank_details(models.Model):
    BANK_ACCOUNT_TYPES = [
        ('Savings', 'Savings'),
        ('Current', 'Current'),
        ('Fixed Deposit', 'Fixed Deposit'),
        ('Recurring Deposit', 'Recurring Deposit'),
        ('NRO', 'NRO'),
        ('NRE', 'NRE'),
        ('FCNR', 'FCNR'),
    ]

    bank_name = models.CharField(max_length=255)
    branch_name = models.CharField(max_length=255)
    IFSC = models.CharField(max_length=11)
    account_name = models.CharField(max_length=255)
    account_no = models.CharField(max_length=20)
    bank_logo = models.ImageField(upload_to='bank_logos/', blank=True, null=True)
    account_type = models.CharField(max_length=50, choices=BANK_ACCOUNT_TYPES)

    def __str__(self):
        return f"{self.bank_name} - {self.branch_name}"

class System_Board_of_Directors(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    date_of_join = models.DateField()
    date_of_leave = models.DateField(null=True, blank=True)
    share = models.FloatField()
    stakeholder = models.BooleanField()
    def __str__(self):
        return self.name

class Department_Name(models.Model):
    departmentid = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255,unique=True)
    status = models.BooleanField()
    def __str__(self):
        return self.name
    
class Department_Designation(models.Model):
    designation = models.CharField(max_length=255)
    dept_name = models.ForeignKey(Department_Name, on_delete=models.CASCADE)
    roles_rights = models.CharField(max_length=20)
    def __str__(self):
        return self.designation
    
class Department_Label(models.Model):
    designation = models.ForeignKey(Department_Designation,on_delete=models.CASCADE)
    label_description = models.TextField()
    status = models.CharField(max_length=20)
    def __str__(self):
        return self.label_description
    
class Department_Grade(models.Model):
    label = models.ForeignKey(Department_Label,on_delete=models.CASCADE)
    grade_description = models.TextField()
    status = models.CharField(max_length=20)
    def __str__(self):
        return self.grade_description
    
# class Team_management(models.Model):
#     team_leader = models.CharField(max_length=255)
#     team_member = models.BigIntegerField()
#     department_id = models.ForeignKey(Department_Name, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"Team for {self.department_id.name}"
    
class Customer(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    present_address = models.TextField()
    present_city = models.CharField(max_length=100)
    present_district = models.CharField(max_length=100)
    present_country = models.CharField(max_length=100)
    present_pincode = models.CharField(max_length=20)
    permanent_address = models.TextField()
    permanent_city = models.CharField(max_length=100)
    permanent_district = models.CharField(max_length=100)
    permanent_country = models.CharField(max_length=100)
    permanent_pincode = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    nationality = models.CharField(max_length=100)
    religion = models.CharField(max_length=100)
    caste = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
