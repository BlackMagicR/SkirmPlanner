from django.shortcuts import render

from django.views.generic import TemplateView

class LoginPage(TemplateView):
    template_name = "login.tmpl"

    def get_context_data(self, **kwargs):
        pass

class LogoutPage(TemplateView):
    template_name = "logout.tmpl"

    def get_context_data(self, **kwargs):
        pass