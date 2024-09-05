from django.db import models

class Roles(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.name}"
    
class Rights(models.Model):
    roles = models.ForeignKey(Roles, on_delete=models.CASCADE)
    view = models.BooleanField(default=False)
    write = models.BooleanField(default=False)
    edit = models.BooleanField(default=False)
    delete = models.BooleanField(default=False)
    # ischecked = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.roles}"