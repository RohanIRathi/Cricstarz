from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

class Tournament(models.Model):
    name = models.CharField(max_length=128, unique=True, validators=[MinLengthValidator(2,'Minimum 2 Characters required')])
    no_of_overs = models.IntegerField()
    no_of_teams = models.IntegerField()
    no_of_players = models.IntegerField("No. of players per team", default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date_time = models.DateTimeField(verbose_name="Start Date and Time")
    end_date_time = models.DateTimeField(verbose_name="End Date and Time")
    venue = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name
