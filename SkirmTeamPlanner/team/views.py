from django.shortcuts import render
from django.views.generic import TemplateView

class TeamPage(TemplateView):
    template_name = "team.tmpl"

    def get_context_data(self, **kwargs):
        pass
        #Is user part of a team? Yes: load team info/ No: load 50/50 page search and join or create team.
