from django.utils import timezone

from domain_model import scrape_league_data
from domain_model import create_stats
from leaguestats.models import League, Player, PlayerGameweekStats, LeaguePlayers

def persist_league_data(league_id, league_metadata, team_data_df):
    league_entry = League(
        league_id=league_id,
        pub_time=timezone.now()
    )
    league_entry.save()

    for player in league_metadata:
        player_entry = Player(
            player_id=player['team_id'],
            name=player['player_name'],
            team_name=player['team_name'],
            pub_time=timezone.now()
        )
        player_entry.save()

        league_players_entry = LeaguePlayers(
            league=league_id,
            player=player['team_id']
        )
        league_players_entry.save()

    for index, row in team_data_df.iterrows():
        PlayerGameweekStats.objects.create(
            player_id=row['ID'],
            gameweek=row['GW'],
            gw_points=row['GP'],
            bench_points=row['PB'],
            transfers_made=row['TM'],
            transfers_cost=row['TC'],
            team_value=row['TV'],
            overall_points=row['OP']
        )


def retrieve_league_data(league_id):
    league_metadata = scrape_league_data.scrape_league_info(league_id)
    team_data = scrape_league_data.scrape_team_data_from_league_info(league_metadata)
    team_data_df = scrape_league_data.convert_data_to_dataframe(team_data)
    persist_league_data(league_id, league_metadata, team_data_df)
    
    return team_data_df

def get_league_stats_data_handler(league_id):
    league_data = retrieve_league_data(league_id)
    stats_obj = create_stats.CreateStats(league_data)
    (gamepoint_top_10, gamepoint_bottom_10) = stats_obj.gamepoint_top_bottom_10()
    cumulative_transfers_made = stats_obj.cumulative_transfers_made()
    gamepoints_by_week = stats_obj.gamepoints_by_week()
    gamepoint_rank = stats_obj.gamepoint_rank()
    overall_point_rank = stats_obj.overall_point_rank()
    bench_points_top_10 = stats_obj.bench_points_top_10()
    team_value_by_week = stats_obj.team_value_by_week()

    data = {
        "cumulative_transfers_made": cumulative_transfers_made,
        "gamepoints_by_week": gamepoints_by_week,
        "gamepoint_rank": gamepoint_rank,
        "gamepoint_top_10": gamepoint_top_10,
        "gamepoint_bottom_10": gamepoint_bottom_10,
        "overall_point_rank": overall_point_rank,
        "bench_points_top_10": bench_points_top_10,
        "team_value_by_week": team_value_by_week,
    }

    return data
