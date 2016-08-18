from django.shortcuts import render
from django.views.generic import TemplateView

class TeamPage(TemplateView):
    template_name = "team.tmpl"

    def get_context_data(self, **kwargs):
        #Is user part of a team? Yes: load team info/ No: load 50/50 join or create team. Perhaps include a search box
