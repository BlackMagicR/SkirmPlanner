from django.shortcuts import render
from django.views.generic import TemplateView

class TeamPage(TemplateView):
    template_name = "team.tmpl"

