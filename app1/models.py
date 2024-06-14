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
    
class System_company_type(models.Model):
    type_name = models.CharField(max_length=100)
    def __str__(self):
        return self.type_name

class System_company_detail(models.Model):
    companyid = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, blank=True, null=True)
    company_type = models.ForeignKey(System_company_type,on_delete=models.CASCADE)
    company_size = models.CharField(max_length=255)
    incorporation_no = models.CharField(max_length=255)
    incorporation_agency = models.CharField(max_length=255)
    date = models.DateField()
    certificate = models.FileField(upload_to='company_certificates/',blank=True,null=True)
    TAX_certificate = models.FileField(upload_to='tax_certificates/',blank=True,null=True)
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
    brand_logo = models.ImageField(upload_to='brand_logos/',blank=True,null=True)
    favicon = models.ImageField(upload_to='favicons/',blank=True,null=True)
    letter_header = models.ImageField(upload_to='letter_headers/',blank=True,null=True)
    letter_footer = models.ImageField(upload_to='letter_footers/',blank=True,null=True)
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
    name = models.CharField(max_length=255)
    URL = models.URLField()
    icon = models.ImageField(upload_to='social_icons/')
    company_id = models.ForeignKey(System_company_detail, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - Social Details ({self.company_id.name})"

class System_other_detail(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField()
    company_id = models.ForeignKey(System_company_detail, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - Other Details ({self.company_id.name})"
    
class System_branch_type(models.Model):
    type_name = models.CharField(max_length=100)
    def __str__(self):
        return self.type_name
    
class Department_Name(models.Model):
    departmentid = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
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
    
class Team_management(models.Model):
    team_leader = models.CharField(max_length=255)
    team_member = models.BigIntegerField()
    department_id = models.ForeignKey(Department_Name, on_delete=models.CASCADE)

    def __str__(self):
        return f"Team for {self.department_id.name}"
    
class Emp_company_profile(models.Model):
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
    emp_id = models.ForeignKey(Emp_company_profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"Address for {self.emp_id.name}"
    
