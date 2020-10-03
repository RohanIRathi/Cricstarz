from django.shortcuts import redirect, render
from django.views.generic import CreateView
from .models import Match
from django.urls import reverse_lazy
from tournament.models import Tournament
from teams.models import Team
from django.http import JsonResponse
from django.contrib import messages

class MatchCreateView(CreateView):
	model = Match
	fields = ['team1', 'team2']
	success_url = reverse_lazy('tournaments:all')
	success_message = "Match Created!!"

	def form_valid(self, form):
		object = form.save(commit=False)
		tournament = Tournament.objects.get(id=self.kwargs.get('tournamentid'))
		if object.team1 in Team.objects.filter(tournament=tournament) and object.team2 in Team.objects.filter(tournament=tournament):
			object.tournament = tournament
			object.save()
			messages.success(self.request, f'Match ceated!!')
			return super(MatchCreateView, self).form_valid(form)
		else:
			messages.error(self.request, f'You selected teams that were not in this tournament!')
			return redirect(f'/match/{tournament.id}/new/')