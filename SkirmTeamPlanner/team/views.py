from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import ModelForm
from django.forms import Textarea

from SkirmTeamPlanner.views import LoggedInMixin
from team.models import TeamMember, Team

class TeamPage(LoggedInMixin, TemplateView):
    template_name = "teams.tmpl"

    def get_context_data(self, **kwargs):
        context = super(TeamPage, self).get_context_data(**kwargs)
        team_members = TeamMember.objects.filter(user=self.request.user)
        teams = Team.objects.all()
        context['team_members'] = team_members
        context['teams'] = teams

        return context
        #Is user part of a team? Yes: load team info/ No: load search and join or create team.

class AddTeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['title', 'description']
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 20}),
        }


class AddTeamPage(LoggedInMixin, FormView):
    template_name = 'add_team.tmpl'
    form_class = AddTeamForm
    success_url = '/teams/'
        
    def form_valid(self, form):
        form.save()
        team_member = TeamMember.objects.create(team=form.instance, user=self.request.user, is_admin=True)
        return super(AddTeamPage, self).form_valid(form)

class TeamDetailView(LoggedInMixin, TemplateView):
    template_name = 'team_details.tmpl'

    def get_context_data(self, **kwargs):
        context = super(TeamDetailView, self).get_context_data(**kwargs)
        context['team'] = Team.objects.get(id=kwargs['pk'])
        context['members'] = TeamMember.objects.filter(team=kwargs['pk'])
        return context
