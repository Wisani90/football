from domain_model import scrape_league_data
from domain_model import create_stats

def get_league_stats_data_handler(league_id):
    league_data_obj = scrape_league_data.ScrapeData(league_id)
    data = league_data_obj.get_data()
    stats_obj = create_stats.CreateStats(data)
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
