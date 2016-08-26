from django.conf.urls import include, url, patterns

from team.views import TeamPage, AddTeamPage, TeamDetailView

urlpatterns = patterns('', 
    url(r'^$', TeamPage.as_view(), name='team'),
    url(r'^add/$', AddTeamPage.as_view(), name='add'),
    url(r'^team/(?P<pk>\d+)/$', TeamDetailView.as_view(), name='teamdetailview')
)