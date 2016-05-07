from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<league_id>\d+)/$', views.results, name='results'),
    url(r'^find_league_number/$', views.find_league_number, name='find_league_number')
]
