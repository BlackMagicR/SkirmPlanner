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

    
    def get(self, request):
        print "My urls are working!"

        return HttpResponse('Jippie')
