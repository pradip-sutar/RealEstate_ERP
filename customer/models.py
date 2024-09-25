from django.db import models



class Customer_Form(models.Model):
    name = models.CharField(max_length=255)
    mob = models.CharField(max_length=15)
    email = models.EmailField()
    present_address = models.TextField()
    present_city = models.CharField(max_length=255)
    present_district = models.CharField(max_length=255)
    present_country = models.CharField(max_length=255)
    present_pincode = models.CharField(max_length=10)
    permanent_address = models.TextField()
    permanent_city = models.CharField(max_length=255)
    permanent_district = models.CharField(max_length=255)
    permanent_country = models.CharField(max_length=255)
    permanent_pincode = models.CharField(max_length=10)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    nationality = models.CharField(max_length=255)
    religion = models.CharField(max_length=255)
    caste = models.CharField(max_length=255)

    def __str__(self):
        return self.name