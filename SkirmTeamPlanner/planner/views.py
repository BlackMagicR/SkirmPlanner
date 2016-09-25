from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.http import HttpResponse
from django.forms import ModelForm

from updater.models import Skirm
from team.models import PlannedEvent
from SkirmTeamPlanner.views import LoggedInMixin

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

class CreateEventForm(ModelForm):
    class Meta:
        model = PlannedEvent
        fields = ['team']

class CreateEventView(LoggedInMixin, FormView):
    template_name = 'create_event.tmpl'
    form_class = CreateEventForm
    success_url = ''

    def get(self, request, *args, **kwargs):
        try:
            self.skirm = Skirm.objects.get(id=kwargs['pk'])
            print self.skirm
        except Exception as e:
            print e
            # pass #Todo: think of a way to handle this
        return super(CreateEventView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CreateEventView, self).get_context_data(**kwargs)
        context['skirm'] = self.skirm
        return context

    def form_valid(self, form):
        print Skirm.objects.get(id=self.kwargs['pk'])
        form.cleaned_data['skirm'] =  Skirm.objects.get(id=self.kwargs['pk'])
        form.save()
        return super(CreateEventView, self).form_valid(form)