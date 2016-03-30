import pandas as pd

def order_by_gameweek(df):
    df['indexNumber'] = [int(i.split(' ')[-1]) for i in df.index]
    df.sort_values('indexNumber', ascending=True, inplace=True)
    df = df.drop('indexNumber', 1)
    return df

class CreateStats():
    def __init__(self, league_data):
        self.league_data = league_data

    def cumulative_transfers_made(self):
        ctm_df_select = self.league_data[['GW', 'TM', 'player_name']]
        ctm_pivot = ctm_df_select.pivot(index='GW', columns='player_name', values='TM')
        ctm_pivot = order_by_gameweek(ctm_pivot)
        ctm_pivot = ctm_pivot.cumsum()
        ctm_dicts = ctm_pivot.to_dict()
        return ctm_dicts

    def gamepoints_by_week(self):
        gpw_df_select = self.league_data[['GW', 'GP', 'player_name']]
        gpw_pivot = gpw_df_select.pivot(index='GW', columns='player_name', values='GP')
        gpw_pivot = order_by_gameweek(gpw_pivot)
        gpw_dicts = gpw_pivot.to_dict()
        return gpw_dicts

    def gamepoint_rank(self):
        df = self.league_data
        df['gp_rank'] = df.groupby('GW')['GP'].rank(ascending=False)
        gpr_select = df[['GW', 'gp_rank', 'player_name']]
        gpr_pivot = gpr_select.pivot(index='GW', columns='player_name', values='gp_rank')
        gpr_pivot = order_by_gameweek(gpr_pivot)
        gpr_dicts = gpr_pivot.to_dict()
        return gpr_dicts

    def gamepoint_top_bottom_10(self):
        gp_sort = self.league_data[['GW', 'GP', 'player_name']].sort_values('GP', ascending=False)
        gp_sort.columns = ['Gameweek', 'Points', 'Name']
        gp_sort_top = gp_sort.head(10)
        gp_sort_bottom = gp_sort.tail(10)
        top_10 = []
        for row in gp_sort_top.index:
            top_dict = {
                'Gameweek': gp_sort_top.loc[row, 'Gameweek'],
                'Name': gp_sort_top.loc[row, 'Name'],
                'Points': gp_sort_top.loc[row, 'Points'],
            }
            top_10.append(top_dict)

        bottom_10 = []
        for row in gp_sort_bottom.index:
            bottom_dict = {
                'Gameweek': gp_sort_bottom.loc[row, 'Gameweek'],
                'Name': gp_sort_bottom.loc[row, 'Name'],
                'Points': gp_sort_bottom.loc[row, 'Points'],
            }
            bottom_10.append(bottom_dict)

        return (top_10, bottom_10)

    def overall_point_rank(self):
        df = self.league_data
        df['op_rank'] = df.groupby('GW')['OP'].rank(ascending=False)
        opr_select = df[['GW', 'op_rank', 'player_name']]
        opr_pivot = opr_select.pivot(index='GW', columns='player_name', values='op_rank')
        opr_pivot = order_by_gameweek(opr_pivot)
        opr_dicts = opr_pivot.to_dict()
        return opr_dicts

    def bench_points_top_10(self):
        bp_sort = self.league_data[['GW', 'PB', 'player_name']].sort_values('PB', ascending=False)
        bp_sort.columns = ['Gameweek', 'Bench Points', 'Name']
        top_10_bp_sort = bp_sort.head(10)
        top_10 = []
        for row in top_10_bp_sort.index:
            top_dict = {
                'Gameweek': top_10_bp_sort.loc[row, 'Gameweek'],
                'Name': top_10_bp_sort.loc[row, 'Name'],
                'Points': top_10_bp_sort.loc[row, 'Bench Points'],
            }
            top_10.append(top_dict)
        return top_10

    def team_value_by_week(self):
        tv_select = self.league_data[['GW', 'TV', 'player_name']]
        tv_pivot = tv_select.pivot(index='GW', columns='player_name', values='TV')
        tv_pivot = order_by_gameweek(tv_pivot)
        tv_dicts = tv_pivot.to_dict()
        return tv_dicts

def main():
    from domain_model.scrape_league_data import ScrapeData
    league = ScrapeData(314488)
    data = league.get_data()
    stats_obj = CreateStats(data)
    print stats_obj.gamepoint_top_bottom_10()


if __name__ == '__main__':
    main()