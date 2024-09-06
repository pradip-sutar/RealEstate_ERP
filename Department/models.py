from django.db import models
from Roles_Rights.models import Roles, Rights
# Create your models here.
class Department_Name(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255,unique=True)
    status = models.BooleanField()
    # roles = models.ForeignKey(Roles, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name
    
class Department_Designation(models.Model):
    designation = models.CharField(max_length=255)
    dept_name = models.ForeignKey(Department_Name, on_delete=models.CASCADE)
    # rights = models.CharField(max_length=50)
    def __str__(self):
        return self.designation
    
class Department_Label(models.Model):
    designation = models.ForeignKey(Department_Designation,on_delete=models.CASCADE)
    label_description = models.TextField()
    status = models.CharField(max_length=50)
    def __str__(self):
        return self.label_description
    
class Department_Grade(models.Model):
    label = models.ForeignKey(Department_Label,on_delete=models.CASCADE)
    grade_description = models.TextField()
    status = models.CharField(max_length=20)
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