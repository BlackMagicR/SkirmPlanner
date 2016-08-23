from django.conf.urls import include, url, patterns

from user.views import ProfilePage

urlpatterns = patterns('', 
    url(r'^$', ProfilePage.as_view(), name='profile'),
)