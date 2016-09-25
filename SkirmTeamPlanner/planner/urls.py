from django.conf.urls import include, url, patterns

from planner.views import SkirmList, SkirmDetailView, CreateEventView

urlpatterns = patterns('', 
    url(r'^$', SkirmList.as_view(), name='agenda'),
    url(r'^skirm/(?P<pk>\d+)/$', SkirmDetailView.as_view(), name='skirmdetailview'),
    url(r'^event/add/(?P<pk>\d+)/$', CreateEventView.as_view(), name='create_event'),
)