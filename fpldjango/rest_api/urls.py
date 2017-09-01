from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^leaguestats/(?P<league_id>\d+)/$',
        views.LeagueStatsView.as_view(),
        name='leaguestatsview')
]
