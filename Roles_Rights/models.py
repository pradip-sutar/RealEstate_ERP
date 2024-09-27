from django.db import models

class Roles(models.Model):
    name = models.JSONField()
    def __str__(self):
        return f"{self.name}"
    
class Rights(models.Model):
    roles_id = models.ForeignKey(Roles, on_delete=models.CASCADE)
    roles_name = models.CharField(max_length=100)
    view = models.BooleanField(default=False)
    write = models.BooleanField(default=False)
    edit = models.BooleanField(default=False)
    delete = models.BooleanField(default=False)
    # ischecked = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.roles_name}"