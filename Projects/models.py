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
    
class Project_subproject_details:
    code=models.IntegerField()
    segment=models.CharField(max_length=100)
    Name=models.CharField(max_length=100)
    layout=models.ImageField(upload_to='Product_subproject_image/')

class Project_Nearby:
    name=models.CharField
    
    
class Project_Product(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    segment = models.ForeignKey(Project_Nearby_Segment, on_delete=models.CASCADE)
    type = models.ForeignKey(Project_Product_Type, on_delete=models.CASCADE)
    variance = models.CharField(max_length=255)
    nos = models.IntegerField()
    area = models.DecimalField(max_digits=10, decimal_places=2)
    layout_image = models.ImageField(upload_to='layout_images/')
    cost = models.DecimalField(max_digits=15, decimal_places=2)
    amenity = models.ForeignKey(Project_Amenity_Master, on_delete=models.CASCADE)
    description = models.TextField()
    confirm_project_id = models.ForeignKey(Confirm_Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Project_add_Payment(models.Model):
    title = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    confirm_project_id = models.ForeignKey(Confirm_Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Project_add_Amenity(models.Model):
    title = models.ForeignKey(Project_Amenity_Master, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='amenities/')
    confirm_project_id = models.ForeignKey(Confirm_Project, on_delete=models.CASCADE)
    def __str__(self):
        return self.title.name
    
class Project_add_Commission(models.Model):
    commission = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    confirm_project_id = models.ForeignKey(Confirm_Project, on_delete=models.CASCADE)
    def __str__(self):
        return self.commission
    
class Project_add_Tax(models.Model):
    name = models.CharField(max_length=255)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    confirm_project_id = models.ForeignKey(Confirm_Project, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Project_add_PaidAmenity(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Paid_amenities/')
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    confirm_project_id = models.ForeignKey(Confirm_Project, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
class Project_add_Price(models.Model):
    name = models.CharField(max_length=255)
    purchase = models.CharField(max_length=255)
    base = models.DecimalField(max_digits=10, decimal_places=2)
    market = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    confirm_project_id = models.ForeignKey(Confirm_Project, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    

class Project_add_Inventory(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    quantity = models.IntegerField()
    build = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    carpet = models.IntegerField()
    sold = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.IntegerField()
    confirm_project_id = models.ForeignKey(Confirm_Project, on_delete=models.CASCADE)
    def __str__(self):
        return self.name