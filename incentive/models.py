from django.db import models

class Goal(models.Model):
  # Target fields
  target_number = models.IntegerField()
  achievement_percentage = models.DecimalField(max_digits=5, decimal_places=2)

  # Goal description fields
  uom = models.CharField(max_length=255)  # Unit of Measurement
  ucm = models.CharField(max_length=255)  # Unit of Change Measurement
  description = models.TextField()

def __str__(self):
        return f"{self.target_number} {self.uom} by {self.ucm}: {self.description}"
