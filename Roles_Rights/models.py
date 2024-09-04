from django.db import models

class Roles(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Rights(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name