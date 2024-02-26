from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ABC(models.Model):
    id = models.AutoField(primary_key=True)
    ab = models.IntegerField(default=0)
    bc = models.TextField(max_length=1000, default="")
    def __str__(self):
        return f"Abc # {self.id}"