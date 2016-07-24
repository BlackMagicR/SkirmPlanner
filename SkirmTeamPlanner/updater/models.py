from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Skirm(models.Model):
    title = models.CharField(max_length=250)
    link = models.CharField(max_length=150)
    date = models.DateField()
    city = models.CharField(max_length=50)

    #We load these items the first time a user loads the skirm page and then save it. That is more effective than visiting all pages using the updater
    description = models.CharField(max_length=5000) 
    street = models.CharField(max_length=100)
    postal = models.CharField(max_length=10)
    organiser = models.CharField(max_length=150)
