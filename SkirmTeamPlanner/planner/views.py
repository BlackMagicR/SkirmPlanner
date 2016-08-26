from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

from updater.models import Skirm
from team.models import PlannedEvent

class BaseSkirmList(TemplateView):
    template_name = 'skirmlist.tmpl'

class SkirmList(BaseSkirmList):

    def get_context_data(self, **kwargs):
        context = super(SkirmList, self).get_context_data(**kwargs)
        context['skirms'] = Skirm.objects.all()
        relevant_events = PlannedEvent.objects.filter(team__id=1).filter(skirm__in=context['skirms'])#place holder id
        return context
    
class SkirmDetailView(TemplateView):
    template_name = 'skirmdetails.tmpl'

    def get_context_data(self, **kwargs):
        context = super(SkirmDetailView, self).get_context_data(**kwargs)
        context['skirm'] = Skirm.objects.get(id=kwargs['pk'])
        return context
