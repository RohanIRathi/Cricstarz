from django.shortcuts import render
from django.views.generic import CreateView
from .models import Team
from django.urls import reverse_lazy
from tournament.models import Tournament

class TeamCreateView(CreateView):
    model = Team
    fields = ['name', 'no_of_players']
    success_url = reverse_lazy('tournaments:all')
    success_message = "Team Created!!"
    
    def get_form(self):
         form = super().get_form()
         return form
     
    def form_valid(self, form):
        object = form.save(commit=False)
        object.tournament = Tournament.objects.get(id=self.kwargs.get('tournamentid'))
        object.save()
        return super(TeamCreateView, self).form_valid(form)