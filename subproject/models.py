from django.db import models

# Product Details Model
class ProductDetail(models.Model):
    code = models.CharField(max_length=100)
    segment = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    variant = models.CharField(max_length=100)
    layout = models.FileField(upload_to='layouts/', null=True, blank=True)
    units = models.IntegerField()

# Raise Cost Model
class RaiseCost(models.Model):
    raise_type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2)

# Product Cost Model
class ProductCost(models.Model):
    product_type_code = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    variant = models.CharField(max_length=100)
    floor_lane = models.CharField(max_length=100)
    facing = models.CharField(max_length=100)
    build_up_area = models.DecimalField(max_digits=10, decimal_places=2)
    carpet_area = models.FileField(upload_to='Area/', null=True, blank=True)
    layout = models.DecimalField(max_digits=10, decimal_places=2)
    units = models.IntegerField()
    unit_costs=models.IntegerField()
    selling_costs=models.IntegerField()

from django.db import models

# Model for Product Cost with detailed information
class ProductCost_1(models.Model):
    product_type_code = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    variant = models.CharField(max_length=100)
    floor_lane = models.CharField(max_length=100)
    facing = models.CharField(max_length=100)
    build_up_area = models.DecimalField(max_digits=10, decimal_places=2)
    carpet_area = models.DecimalField(max_digits=10, decimal_places=2)
    layout = models.FileField(upload_to='layouts/', null=True, blank=True)
    units=models.IntegerField()
    units_number=models.IntegerField()

    def __str__(self):
        return self.product_type_code

# Model for Product Cost related to amenities or other features
class AmenityCost(models.Model):
    type = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    images = models.FileField(upload_to='amenities/', null=True, blank=True)

    def __str__(self):
        return self.type


