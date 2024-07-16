from django.db import models


class Product_Payment_Schedule(models.Model):
    title = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.title

class Product_Amenity_Master(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_amenity/')
    def __str__(self):  
        return self.title

class Product_Commission(models.Model):
    commission = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.commission}% - {self.amount}"
    
class Product_LayoutImage(models.Model):
    image = models.ImageField(upload_to='Product_LayoutImage/')
    def __str__(self):
        return self.image
    
class Product_Dynamic_Spec(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title
  