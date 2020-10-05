from django.db import models
from tournament.models import Tournament

class Team(models.Model):
    name = models.CharField("Team Name", max_length=128)
    runs = models.IntegerField(verbose_name="Total Runs Scored by Team", default=0)
    fours = models.IntegerField(verbose_name="Total Fours by Team", default=0)
    sixes = models.IntegerField(verbose_name="Total Sixes by Team", default=0)
    wides = models.IntegerField(verbose_name="Total Wides Thrown by Team", default=0)
    noballs = models.IntegerField(verbose_name="Total No Balls by Team", default=0)
    matcheswon = models.IntegerField(verbose_name="Total Matches Won by Team", default=0)
    
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name