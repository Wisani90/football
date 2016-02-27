# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from getdata import *

df = df.reset_index(level=0)
    
gp_select = df[['GW','GP','ID']]

gp_pivot = gp_select.pivot(index='GW', columns='ID', values='GP')

#Ensures ordering by gameweek
gp_pivot['indexNumber'] = [int(i.split(' ')[-1]) for i in gp_pivot.index]
gp_pivot.sort(['indexNumber'], ascending = [True], inplace = True)
gp_pivot = gp_pivot.drop('indexNumber', 1)
print gp_pivot


import plotly.plotly as py
import plotly.graph_objs as go


layout = go.Layout(
    yaxis=dict(
        title='Number of points'
        )
    )

fig=go.Figure(data=[{
    'x': gp_pivot.index,
    'y': gp_pivot[col],
    'name': col
}  for col in gp_pivot.columns],
layout=layout)

plot_url = py.plot(fig, filename='gp_by_gameweek_11')