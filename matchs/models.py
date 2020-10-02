from django.db import models
from tournament.models import Tournament
from teams.models import Team

class Match(models.Model):
    team1 = models.ForeignKey(Team, on_delete=models.PROTECT, related_name="team1")
    team2 = models.ForeignKey(Team, on_delete=models.PROTECT, related_name="team2")
    tournament = models.ForeignKey(Tournament, on_delete=models.PROTECT)
    winner = models.ForeignKey(Team, on_delete=models.PROTECT, related_name="winner")
    
    def __str__(self):
        return self.team1.name + " vs " + self.team2.name
