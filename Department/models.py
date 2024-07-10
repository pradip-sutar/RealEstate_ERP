from django.db import models

# Create your models here.
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
    
