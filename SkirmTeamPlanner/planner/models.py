from django.db import models

from updater.models import Skirm
# from team.models import Team

class PlannedEvent(models.Model):
    skirm = models.ForeignKey(Skirm, on_delete=models.CASCADE)
    # team = models.ForeignKey(Team, on_delete=models.CASCADE)


    