import math

def order_by_gameweek(df):
    df['indexNumber'] = [int(i.split(' ')[-1]) for i in df.index]
    df.sort_values('indexNumber', ascending=True, inplace=True)
    df = df.drop('indexNumber', 1)
    return df

class CreateStats(object):
    def __init__(self, league_data):
        self.league_data = league_data
        self.league_data.fillna(0, inplace=True)

    def cumulative_transfers_made(self):
        ctm_df_select = self.league_data[['GW', 'TM', 'player_name']]
        top_10 = list(ctm_df_select.groupby('player_name').sum().sort_values(
            'TM', ascending=False).head(10).index)
        ctm_df_select = ctm_df_select[ctm_df_select['player_name'].isin(top_10)]
        ctm_pivot = ctm_df_select.pivot(index='GW', columns='player_name', values='TM')
        ctm_pivot = order_by_gameweek(ctm_pivot)
        ctm_pivot = ctm_pivot.cumsum()
        ctm_pivot.fillna(0, inplace=True)
        ctm_list_of_lists = []
        gameweek_list = ['Gameweek']
        for gameweek in ctm_pivot.index:
            gameweek_int = int(gameweek.split(' ')[1])
            gameweek_list.append(gameweek_int)
        ctm_list_of_lists.append(gameweek_list)
        for name in ctm_pivot.columns.values.tolist():
            name_list = [name]
            name_list.extend(ctm_pivot[name].tolist())
            ctm_list_of_lists.append(name_list)
        return ctm_list_of_lists

    def gamepoints_by_week(self):
        gpw_df_select = self.league_data[['GW', 'GP', 'player_name']]
        gpw_pivot = gpw_df_select.pivot(index='GW', columns='player_name', values='GP')
        gpw_average = gpw_df_select[['GW', 'GP']].groupby('GW').mean()
        gpw_pivot = order_by_gameweek(gpw_pivot)
        gpw_pivot.fillna(0, inplace=True)
        gpw_list_of_lists = []
        gameweek_list = ['Gameweek']
        average_list = ['Average']
        for gameweek in gpw_pivot.index:
            gameweek_int = int(gameweek.split(' ')[1])
            gameweek_list.append(gameweek_int)
            average_list.append(gpw_average.loc[gameweek, 'GP'])
        gpw_list_of_lists.append(gameweek_list)
        gpw_list_of_lists.append(average_list)
        for name in gpw_pivot.columns.values.tolist():
            name_list = [name]
            name_list.extend(gpw_pivot[name].tolist())
            gpw_list_of_lists.append(name_list)
        return gpw_list_of_lists

    def gamepoint_rank(self):
        df = self.league_data
        df['gp_rank'] = df.groupby('GW')['GP'].rank(ascending=False)
        gpr_select = df[['GW', 'gp_rank', 'player_name']]
        gpr_pivot = gpr_select.pivot(index='GW', columns='player_name', values='gp_rank')
        gpr_pivot = order_by_gameweek(gpr_pivot)
        gpr_pivot.fillna(len(gpr_pivot.columns.values), inplace=True)
        gpr_dicts = gpr_pivot.to_dict()
        return gpr_dicts

    def gamepoint_top_bottom_10(self):
        gp_sort = self.league_data[['GW', 'GP', 'player_name']].sort_values('GP', ascending=False)
        gp_sort.columns = ['Gameweek', 'Points', 'Name']
        gp_sort_top = gp_sort.head(10)
        gp_sort_bottom = gp_sort.sort_values('Points', ascending=True).head(10)
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
        opr_select['op_rank'] = opr_select['op_rank'].apply(lambda x: int(math.floor(x)))
        opr_pivot = opr_select.pivot(index='GW', columns='player_name', values='op_rank')
        opr_pivot = order_by_gameweek(opr_pivot)
        opr_pivot.fillna(len(opr_pivot.columns.values), inplace=True)
        opr_list_of_lists = []
        gameweek_list = ['Gameweek']
        for gameweek in opr_pivot.index:
            gameweek_int = int(gameweek.split(' ')[1])
            gameweek_list.append(gameweek_int)
        opr_list_of_lists.append(gameweek_list)
        for name in opr_pivot.columns.values.tolist():
            name_list = [name]
            name_list.extend(opr_pivot[name].tolist())
            opr_list_of_lists.append(name_list)
        return opr_list_of_lists

    def bench_points_top_10(self):
        bp_sort = self.league_data[['GW', 'PB', 'player_name']].sort_values('PB', ascending=False)
        bp_sort.columns = ['Gameweek', 'Bench Points', 'Name']
        top_10_bp_sort = bp_sort.head(10)
        top_10 = []
        for row in top_10_bp_sort.index:
            top_dict = {
                'Gameweek': top_10_bp_sort.loc[row, 'Gameweek'],
                'Name': top_10_bp_sort.loc[row, 'Name'],
                'Points': int(top_10_bp_sort.loc[row, 'Bench Points']),
            }
            top_10.append(top_dict)
        return top_10

    def normalised_bench_points_top_10(self):
        normal_bp_sort = self.league_data[['GW', 'PB', 'GP', 'player_name']]
        normal_bp_sort['normalised'] = normal_bp_sort['PB'] / normal_bp_sort['GP']
        normal_bp_sort = normal_bp_sort.sort_values('normalised', ascending=False)
        normal_bp_sort = normal_bp_sort.drop('normalised', axis=1)
        normal_bp_sort.columns = ['Gameweek', 'Bench_Points', 'Gameweek_Points', 'Name']
        top_10_bp_sort = normal_bp_sort.head(10)
        top_10 = []
        for row in top_10_bp_sort.index:
            top_dict = {
                'Gameweek': top_10_bp_sort.loc[row, 'Gameweek'],
                'Name': top_10_bp_sort.loc[row, 'Name'],
                'Bench_Points': top_10_bp_sort.loc[row, 'Bench_Points'],
                'Gameweek_Points': top_10_bp_sort.loc[row, 'Gameweek_Points'],
            }
            top_10.append(top_dict)
        return top_10

    def team_value_by_week(self):
        tv_select = self.league_data[['GW', 'TV', 'player_name']]
        top_10 = list(tv_select.groupby('player_name').sum().sort_values(
            'TV', ascending=False).head(10).index)
        tv_select = tv_select[tv_select['player_name'].isin(top_10)]
        tv_pivot = tv_select.pivot(index='GW', columns='player_name', values='TV')
        tv_pivot = order_by_gameweek(tv_pivot)
        tv_pivot.fillna(100, inplace=True)
        tv_list_of_lists = []
        gameweek_list = ['Gameweek']
        for gameweek in tv_pivot.index:
            gameweek_int = int(gameweek.split(' ')[1])
            gameweek_list.append(gameweek_int)
        tv_list_of_lists.append(gameweek_list)
        for name in tv_pivot.columns.values.tolist():
            name_list = [name]
            name_list.extend(tv_pivot[name].tolist())
            tv_list_of_lists.append(name_list)
        return tv_list_of_lists

def main():
    from domain_model.scrape_league_data import ScrapeData
    league = ScrapeData(314488)
    data = league.get_data()
    stats_obj = CreateStats(data)
    print stats_obj.gamepoint_top_bottom_10()


if __name__ == '__main__':
    main()