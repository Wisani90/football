from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^leaguestats/(?P<league_id>[0-9]+)/$',
        views.LeagueStatsView.as_view(),
        name='leaguestatsview')
]
