from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from domain_model import handlers

import pandas as pd

class LeagueStatsView(APIView):
    def get(self, request, league_id):
        data = handlers.get_league_stats_data_handler(league_id)
        return Response(data)
