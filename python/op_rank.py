# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from getdata import *

df = df.reset_index(level=0)
df['op_rank'] = df.groupby('GW')['OP'].rank(ascending=False)


op_all = pd.DataFrame()

for player in players:
    op_all[player['ID']['Gameweek 1']] = player['OP']
    



op_select = df[['GW','op_rank','ID']]

op_pivot = op_select.pivot(index='GW', columns='ID', values='op_rank')

#Ensures ordering by gameweek
op_pivot['indexNumber'] = [int(i.split(' ')[-1]) for i in op_pivot.index]
op_pivot.sort(['indexNumber'], ascending = [True], inplace = True)
op_pivot = op_pivot.drop('indexNumber', 1)
print op_pivot

import plotly.plotly as py
import plotly.graph_objs as go


layout = go.Layout(
    yaxis=dict(
        autorange='reversed',
        dtick=1,
        title='Rank by overall points'
        )
    )

fig=go.Figure(data=[{
    'x': op_pivot.index,
    'y': op_pivot[col],
    'name': col
}  for col in op_pivot.columns],
layout=layout)

plot_url = py.plot(fig, filename='rank_by_gameweek_11')

