from django.db import models
from tournament.models import Tournament
from teams.models import Team
from matchs.models import Match

class Player(models.Model):
    name = models.CharField("Player Name", max_length=64)
    runs = models.IntegerField(verbose_name="Total Runs", default=0)
    wickets = models.IntegerField(verbose_name="Total Wickets Taken", default=0)
    fours = models.IntegerField(verbose_name="Total Fours", default=0)
    sixes = models.IntegerField(verbose_name="Total sixes", default=0)
    noballs = models.IntegerField(verbose_name="No Balls", default=0)
    wides = models.IntegerField(verbose_name="Wides", default=0)
    runsgiven = models.IntegerField(verbose_name="Runs Given", default=0)
    
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    tournament = models.ForeignKey(Tournament, on_delete=models.PROTECT)

    def __str__(self):
        return self.name