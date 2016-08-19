"""SkirmTeamPlanner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from user.views import LoginPage, LogoutPage

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^agenda/', include('planner.urls', namespace='planner', app_name='planner')),
    url(r'^team/', include('team.urls', namespace='team', app_name='team')),

    url(r'^login/$', LoginPage.as_view(), name='login'),
    url(r'^logout/$', LogoutPage.as_view(), name='logout')
]
