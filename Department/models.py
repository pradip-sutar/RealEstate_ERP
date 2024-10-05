from django.db import models
from Roles_Rights.models import Roles, Rights



# Create your models here.
class Department_Name(models.Model):
    name = models.CharField(max_length=255,unique=True)
    status = models.BooleanField()
    document_rights=models.JSONField(blank=True, null=True)


    # roles = models.ForeignKey(Roles, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name
    
class Department_Designation(models.Model):
    designation = models.CharField(max_length=255)
    dept_name = models.ForeignKey(Department_Name, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    # rights = models.CharField(max_length=50)
    def __str__(self):
        return self.designation
    
class Department_Grade(models.Model):
    level = models.CharField(max_length=100)
    grade_description = models.TextField()
    def __str__(self):
        return self.grade_description
    
class Department_Roles_Rights(models.Model):
    role_id = models.ForeignKey(Roles, on_delete=models.CASCADE)
    role_name = models.CharField(max_length=50)
    view = models.BooleanField(default=False, blank=True,null=True)
    write = models.BooleanField(default=False, blank=True,null=True)
    edit = models.BooleanField(default=False, blank=True,null=True)
    delete = models.BooleanField(default=False, blank=True,null=True)
    department_id = models.ForeignKey(Department_Name, on_delete=models.CASCADE)
    def __str__(self):
        return self.role_name