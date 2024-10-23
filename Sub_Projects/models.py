from django.db import models
from Project_Project.models import *

# 1. Product Details Model
class ProductDetails(models.Model):
    code = models.CharField(max_length=100)
    segment = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    variant = models.CharField(max_length=100)
    layout = models.ImageField(upload_to='product_details_layouts/')
    units = models.IntegerField()
    subproject_id = models.ForeignKey(Project_subproject_details, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code} - {self.product_type}"

# 2. Raise Cost Model
class RaiseCost(models.Model):
    raise_type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    subproject_id = models.ForeignKey(Project_subproject_details, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.raise_type} - {self.name}"

# 3. Product Cost Model
class ProductCost(models.Model):
    product_type_code = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    variant = models.CharField(max_length=100)
    floor_lane = models.CharField(max_length=100)
    facing = models.CharField(max_length=100)
    build_up_area = models.CharField(max_length=100)
    carpet_area = models.CharField(max_length=100)
    layout = models.ImageField(upload_to='product_cost_layouts/')
    units = models.BigIntegerField()
    units_cost = models.BigIntegerField()
    selling_cost = models.BigIntegerField()
    subproject_id = models.ForeignKey(Project_subproject_details, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product_type_code} - {self.product_type}"
    
class ProductInventories(models.Model):
    product_type_code = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    variant = models.CharField(max_length=100)
    floor_lane = models.CharField(max_length=100)
    facing = models.CharField(max_length=100)
    build_up_area = models.CharField(max_length=100)
    carpet_area = models.CharField(max_length=100)
    layout = models.ImageField(upload_to='product_cost_layouts/')
    units = models.BigIntegerField()
    units_number = models.CharField(max_length=200)
    subproject_id = models.ForeignKey(Project_subproject_details, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product_type_code} - {self.product_type}"

class SubProductImages(models.Model):
    type = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    images = models.ImageField(upload_to='sub_product_images/')
    subproject_id = models.ForeignKey(Project_subproject_details, on_delete=models.CASCADE)

    def __str__(self):
        return self.type

class PaymentSlab(models.Model):
    segment = models.CharField(max_length=100)
    milestones = models.CharField(max_length=100)
    payment_slab = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    subproject_id = models.ForeignKey(Project_subproject_details, on_delete=models.CASCADE)

    def __str__(self):
        return self.segment