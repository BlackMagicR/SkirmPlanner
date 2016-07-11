from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TeamMember(models.Model):
    member_status = models.CharField(max_length=100)
    user_profile = models.ForeignKey(User)

class Team(models.Model):
    title = models.CharField(max_length=100)
    team_members = models.ManyToManyField(TeamMember)
    team_logo = models.ImageField()
    description = models.CharField(max_length=500)

