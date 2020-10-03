from django.shortcuts import render
from django.views.generic import View, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .models import *

from bootstrap_datepicker_plus import DateTimePickerInput
from matchs.models import Match
from teams.models import Team

class TournamentListView(LoginRequiredMixin, View):
    def get(self, request):
        tl = Tournament.objects.all().filter(user=self.request.user)

        ctx = {'tournament_list': tl}
        return render(request, 'tournament/tournament_list.html', ctx)

class TournamentCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Tournament
    fields = ['name', 'no_of_overs', 'no_of_teams', 'start_date_time', 'end_date_time', 'venue',]
    success_url = reverse_lazy('tournaments:all')
    success_message = "Tournament Created!!"
    
    def get_form(self):
         form = super().get_form()
         form.fields['start_date_time'].widget = DateTimePickerInput()
         form.fields['end_date_time'].widget = DateTimePickerInput()
         return form
     
    def form_valid(self, form):
        print('form_valid called')
        object = form.save(commit=False)
        object.user = self.request.user
        object.save()
        return super(TournamentCreateView, self).form_valid(form)
    
class TournamentDetailView(DetailView):
    model = Tournament
    template_name = "tournament/tournament_view.html"
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['match_list'] = Match.objects.filter(tournament=kwargs.get('object'))
        context['teamscount'] = Team.objects.filter(tournament=kwargs.get('object')).count()
        print(context.get('teamscount'), context.get('tournament.no_of_teams'))
        return context