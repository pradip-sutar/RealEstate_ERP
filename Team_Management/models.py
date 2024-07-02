from django.db import models

# Create your models here.
class Team_Management(models.Model):
    department = models.CharField(max_length=100)
    team_name = models.CharField(max_length=100)
    team_leader = models.CharField(max_length=100)
    team_members = models.TextField()

    def __str__(self):
        return self.team_name