from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Skirm(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=5000) #We load the description the first time a user loads the skirm page and then save it. That is more effective than visiting all pages in the updater
    city = models.CharField(max_length=50) #We can load this from the events page.
    street = models.CharField(max_length=100)
    postal = models.CharField(max_length=10)
    organiser = models.CharField(max_length=150)
    link = models.CharField(max_length=150)
    date = models.DateField()
    joined_members = models.ManyToManyField(User)
    planned = models.BooleanField()

    
