from django.shortcuts import redirect, render
from django.views.generic import CreateView
from teams.models import Team
from django.urls import reverse_lazy
from tournament.models import Tournament
from .models import Player
from django.contrib import messages

class PlayerCreateView(CreateView):
    model = Player
    fields = ['name', 'team']
    success_url = reverse_lazy('tournaments:all')
    success_message = "Player Added!!"
    
    def form_valid(self, form):
        object = form.save(commit=False)
        object.tournament = Tournament.objects.get(id=self.kwargs.get('tournamentid'))
        if object.team in Team.objects.filter(tournament=object.tournament):
            object.save()
            return super(PlayerCreateView, self).form_valid(form)
        else:
            messages.error(self.request, f'Please select a team from this tournament')
            return redirect(f'/player/{self.kwargs.get("tournamentid")}/new/')