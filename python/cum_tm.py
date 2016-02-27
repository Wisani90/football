# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from getdata import *

df = df.reset_index(level=0)
    
tm_select = df[['GW','TM','ID']]

tm_pivot = tm_select.pivot(index='GW', columns='ID', values='TM')





#Ensures ordering by gameweek
tm_pivot['indexNumber'] = [int(i.split(' ')[-1]) for i in tm_pivot.index]
tm_pivot.sort(['indexNumber'], ascending = [True], inplace = True)
tm_pivot = tm_pivot.drop('indexNumber', 1)
tm_pivot = tm_pivot.cumsum()
print tm_pivot


import plotly.plotly as py
import plotly.graph_objs as go


layout = go.Layout(
    yaxis=dict(
        title='Cumulative transfers made'
        )
    )

fig=go.Figure(data=[{
    'x': tm_pivot.index,
    'y': tm_pivot[col],
    'name': col
}  for col in tm_pivot.columns],
layout=layout)

plot_url = py.plot(fig, filename='cumulative_transfers')