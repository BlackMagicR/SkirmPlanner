from django.conf.urls import include, url, patterns

from planner.views import SkirmList, SkirmDetailView

urlpatterns = patterns('', 
    url(r'^', SkirmList.as_view(), name='agenda'),
    url(r'^skirm/(?P<skirm_id>\d+)/$', SkirmDetailView.as_view(), name='skirmdetailview')
)