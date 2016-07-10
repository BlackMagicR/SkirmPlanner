from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Skirm(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateField()
    joined_members = models.ManyToManyField(User)
    planned = models.BooleanField()

    
