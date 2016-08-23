from django.conf.urls import include, url, patterns

from team.views import TeamPage

urlpatterns = patterns('', 
    url(r'^$', TeamPage.as_view(), name='team'),
)