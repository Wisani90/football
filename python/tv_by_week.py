# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from getdata import *

df = df.reset_index(level=0)
    
tv_select = df[['GW','TV','ID']]

tv_pivot = tv_select.pivot(index='GW', columns='ID', values='TV')

#Ensures ordering by gameweek
tv_pivot['indexNumber'] = [int(i.split(' ')[-1]) for i in tv_pivot.index]
tv_pivot.sort(['indexNumber'], ascending = [True], inplace = True)
tv_pivot = tv_pivot.drop('indexNumber', 1)
print tv_pivot


import plotly.plotly as py
import plotly.graph_objs as go


layout = go.Layout(
    yaxis=dict(
        title='Team Value'
        )
    )

fig=go.Figure(data=[{
    'x': tv_pivot.index,
    'y': tv_pivot[col],
    'name': col
}  for col in tv_pivot.columns],
layout=layout)

plot_url = py.plot(fig, filename='tv_by_gameweek_11')