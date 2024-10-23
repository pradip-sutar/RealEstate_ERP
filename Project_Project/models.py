from django.db import models
from Pre_Project.models import *
from Projects.models import *

#=============================  project tab models ====================================#

class Project_subproject_details(models.Model):
    code = models.AutoField(primary_key=True)
    segment=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    layout=models.ImageField(upload_to='Product_subproject_image/')
    descriptions=models.TextField()
    confirm_project_id = models.ForeignKey(Confirm_Project,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Project_Commission(models.Model):
    code = models.AutoField(primary_key=True)
    segment = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    variant = models.CharField(max_length=255)
    commission = models.CharField(max_length=255)  # Can be Value/% as in the table
    confirm_project_id = models.ForeignKey(Confirm_Project,on_delete=models.CASCADE)

class Project_PaymentSlab(models.Model):
    code = models.AutoField(primary_key=True)
    segment = models.CharField(max_length=255)
    milestone = models.CharField(max_length=255)
    payment_slab = models.CharField(max_length=255)  # Payment terms like 10% of product value
    confirm_project_id = models.ForeignKey(Confirm_Project,on_delete=models.CASCADE)


# Tax Model
class Project_Tax(models.Model):
    code = models.AutoField(primary_key=True)
    segment = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    variant = models.CharField(max_length=255)
    tax = models.CharField(max_length=255)  # Tax can be represented as percentage (%)
    confirm_project_id = models.ForeignKey(Confirm_Project,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.segment} - {self.product_type}"

# Amenity Model
class Project_Amenity(models.Model):
    code = models.AutoField(primary_key=True)
    amenity = models.CharField(max_length=255)
    amenity_type = models.CharField(max_length=255)  # Paid/Free
    category = models.CharField(max_length=255)  # Example: Project
    confirm_project_id = models.ForeignKey(Confirm_Project,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.amenity} - {self.amenity_type}"

# Paid Amenity Model
class Project_PaidAmenity(models.Model):
    code = models.AutoField(primary_key=True)
    amenity = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)  # Example: Project
    confirm_project_id = models.ForeignKey(Confirm_Project,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.amenity} - {self.amount}"

class NearBy(models.Model):
    confirm_project = models.ForeignKey(Confirm_Project, on_delete=models.CASCADE)
    type = models.ForeignKey(Project_Nearby_Segment,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    distance = models.CharField(max_length=255)
    map_url = models.URLField()

class ProjectSpecification(models.Model):
    confirm_project = models.ForeignKey(Confirm_Project, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    description = models.TextField()

class ProjectImages(models.Model):
    confirm_project = models.ForeignKey(Confirm_Project, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    description = models.TextField()
    images = models.ImageField(upload_to='project_images/')
