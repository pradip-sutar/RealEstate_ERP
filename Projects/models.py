from django.db import models
from Pre_Project.models import *
# Create your models here.
class Project_Type(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class Project_Payment_Schedule(models.Model):
    stages = models.CharField(max_length=255)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.CharField(max_length=100)

    def __str__(self):
        return self.stages
    
class Project_Product_Type(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Project_RaiseCost_Type(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Project_Amenity_Master(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Project_Nearby_Segment(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Project_Facing_Master(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Project_Commission(models.Model):
    product_type = models.ForeignKey(Project_Product_Type, on_delete=models.CASCADE)
    commission = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product_type.name} - {self.commission}%"

class Product_Ownership(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product_ApprovalBody(models.Model):
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Project_Tax(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Segment(models.Model):
    name = models.CharField(max_length=255)

class Varient(models.Model):
    name = models.CharField(max_length=255)