import requests
import json

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.urlresolvers import reverse

from leaguestats.forms import PostForm

class RemoteHttpError(Exception):
    def __init__(self, body, status):
        self.body = body
        self.status = status


def get(url):
    res = requests.get(url)
    if not res.status_code == 200:
        raise RemoteHttpError(res.text, status=res.status_code)
    else:
        return res


def index(request):
    league_num_url = request.build_absolute_uri(reverse('find_league_number'))
    if request.method == 'GET':
        form = PostForm()        
    else:
        # A POST request: Handle Form Upload
        form = PostForm(request.POST) # Bind data from request.POST into a PostForm
 
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            league_id = form.cleaned_data['league_id']
            return HttpResponseRedirect(reverse('results',
                                                kwargs={'league_id': league_id}))

    return render(request, 'leaguestats/index.html', {
        'form': form,
        'league_num_url': league_num_url,
    })

def results(request, league_id):
    res = get(request.build_absolute_uri(reverse('leaguestatsview', kwargs={'league_id': league_id})))
    data = eval(res.content)
    context = {
        "cumulative_transfers_made": data['cumulative_transfers_made'],
        "gamepoints_by_week": data['gamepoints_by_week'],
        "gamepoint_rank": data['gamepoint_rank'],
        "gamepoint_top_10": data['gamepoint_top_10'],
        "gamepoint_bottom_10": data['gamepoint_bottom_10'],
        "overall_point_rank": data['overall_point_rank'],
        "bench_points_top_10": data['bench_points_top_10'],
        "team_value_by_week": data['team_value_by_week'],
    }
    return render(request, 'leaguestats/results.html', context)

def find_league_number(request):
    return render(request, 'leaguestats/find_league_number.html')
