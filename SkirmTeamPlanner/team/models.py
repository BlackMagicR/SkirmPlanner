from django.db import models
from django.contrib.auth.models import User

from updater.models import Skirm

class Team(models.Model):
    title = models.CharField(max_length=100)
    team_members = models.ManyToManyField(User, through='TeamMember')
    team_logo = models.ImageField()
    description = models.CharField(max_length=500)
    #Doing the following will allow us to add more information to the skirm using the relationship. For instance:
    #You want to add the members joining this event to a model in the database but it makes no sense to add them to the Skirm model since it is unique to every PlannedEvent.
    planned_skirms = models.ManyToManyField(Skirm, through='PlannedEvent')

class TeamMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, default=None)
    member_status = models.CharField(max_length=100, default="")
    is_admin = models.BooleanField(default=False)

class PlannedEvent(models.Model):
    skirm = models.ForeignKey(Skirm, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

