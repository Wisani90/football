import requests

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
    context = {
    'data': res.content
    }
    return render(request, 'leaguestats/results.html', context)

def find_league_number(request):
    return render(request, 'leaguestats/find_league_number.html')
