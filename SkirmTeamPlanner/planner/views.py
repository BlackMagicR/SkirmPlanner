from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

from updater.models import Skirm

class BaseSkirmList(TemplateView):
    template_name = 'skirmlist.tmpl'

class SkirmList(BaseSkirmList):

    def get_context_data(self, **kwargs):
        context = super(SkirmList, self).get_context_data(**kwargs)
        context['skirms'] = Skirm.objects.all()
        return context
    
class SkirmDetailView(TemplateView):
    template_name = 'skirmdetails.tmpl'
    
    def get(self, request, *args, **kwargs):
        print "GET"
        return super(SkirmDetailView, self).get(request, *arg, **kwargs)

    def get_context_data(self, **kwargs):
        print "GET MY CONTEXT DATAs"
        context = super(SkirmDetailView, self).get_context_data(**kwargs)
        context['skirm'] = Skirm.objects.get(id=81)
        return context
