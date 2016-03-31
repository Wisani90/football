import re
import urllib2

from bs4 import BeautifulSoup
import pandas as pd

def clean_data(df):
    df['GP'] = df['GP'].map(lambda x: float(x))
    df['OR'] = df['OR'].map(lambda x: re.sub(',', '', x))
    df['OP'] = df['OP'].map(lambda x: re.sub(',', '', x))
    df['OP'] = df['OP'].map(lambda x: float(x))
    df['GR'] = df['GR'].map(lambda x: re.sub(',', '', x))
    df['GR'] = df['GR'].map(lambda x: re.sub('-', '0', x))
    df['GR'] = df['GR'].map(lambda x: float(x))
    df['PB'] = df['PB'].map(lambda x: float(x))
    df['TC'] = df['TC'].map(lambda x: float(x))
    df['TM'] = df['TM'].map(lambda x: float(x))
    df['TV'] = df['TV'].map(lambda x: x[1:])
    df['TV'] = df['TV'].map(lambda x: x.rstrip('m'))
    df['TV'] = df['TV'].map(lambda x: float(x))
    return df


def scrape_league_info(league_id):
    url = 'http://fantasy.premierleague.com/my-leagues/{}/standings/'.format(league_id)

    raw_league_data = BeautifulSoup(urllib2.urlopen(url).read(), "lxml")

    all_teams_metadata = []

    for row in raw_league_data('table')[0].findAll('tr')[1:]:
        tds = row('td')
        id_str = (str(tds[2].a))
        try:
            team_id = re.search('entry/(.+?)/event', id_str).group(1)
        except AttributeError:
            # id not found
            team_id = '' # apply your error handling

        team_name = tds[2].string
        player_name = tds[3].string

        team_info = {
            "player_name": player_name,
            "team_name": team_name,
            "team_id": team_id
        }

        all_teams_metadata.append(team_info)

    return all_teams_metadata

def scrape_team_data_from_league_info(all_teams_metadata):

    all_teams_data = []

    for teams in all_teams_metadata:
        url = 'http://fantasy.premierleague.com/entry/{}/history/'.format(teams["team_id"])

        raw_team_data = BeautifulSoup(urllib2.urlopen(url).read(), "lxml")

        player_data = []


        for row in raw_team_data('table')[0].findAll('tr')[1:]:
            tds = row('td')
            data = {
                'ID': teams["team_id"],
                'GW': tds[0].string,
                'GP': tds[1].string,
                'PB': tds[2].string,
                'GR': tds[3].string,
                'TM': tds[4].string,
                'TC': tds[5].string,
                'TV': tds[6].string,
                'OP': tds[7].string,
                'OR': tds[8].string,
                'player_name': teams["player_name"],
                'team_name': teams["team_name"],
            }
            player_data.append(data)

        all_teams_data.extend(player_data)

    return all_teams_data

def convert_data_to_dataframe(all_teams_data):
    df = pd.DataFrame.from_records(all_teams_data)
    df = clean_data(df)
    return df


    