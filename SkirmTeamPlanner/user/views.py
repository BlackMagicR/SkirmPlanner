from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from SkirmTeamPlanner.views import LoggedInMixin


class LoginPage(FormView):
    template_name = "login.tmpl"

    def get_context_data(self, **kwargs):
        pass


class LogoutPage(TemplateView):
    template_name = "logout.tmpl"

    def get_context_data(self, **kwargs):
        pass


class ProfilePage(LoggedInMixin, TemplateView):
    template_name = "profile.tmpl"
    
#The following code will be used once it is up and running
# class RegisterPage(TemplateView):
#     template_name = "register.tmpl"

    
# class RegisterForm(ModelForm):
#     model = User
#     fields = ['email', 'first_name', 'last_name', 'username', 'password']