from django.shortcuts import render
from django.views.generic import TemplateView

from SkirmTeamPlanner.views import LoggedInMixin
from team.models import TeamMember, Team

class TeamPage(LoggedInMixin, TemplateView):
    template_name = "team.tmpl"

    def get_context_data(self, **kwargs):
        context = super(TeamPage, self).get_context_data(**kwargs)
        team_members = TeamMember.objects.filter(user=self.request.user)
        context['team_members'] = team_members
        return context
        #Is user part of a team? Yes: load team info/ No: load search and join or create team.
