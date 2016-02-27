# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

allplayers = pd.read_excel('http://docs.google.com/spreadsheets/d/11OjbFzVDcXCY_g2LzxW579V7q5J9HpusDxmdleIrfEE/pub?output=xlsx', sheetname=None,  index_col='GW')

Ben = allplayers['Ben']
Tim = allplayers['Tim']
Jerome = allplayers['Jerome']
JJ = allplayers['JJ']
George = allplayers['George']
Emily = allplayers['Emily']
Matt = allplayers['Matt']
Fozz = allplayers['Fozz']
Phil = allplayers['Phil']
Angelo = allplayers['Angelo']
Marco = allplayers['Marco']

players = [Ben, Tim, Jerome, JJ, George, Emily, Matt, Fozz, Phil, Angelo, Marco]

Ben['ID'] = 'Ben'
Tim['ID'] = 'Tim'
Jerome['ID'] = 'Jerome'
JJ['ID'] = 'JJ'
George['ID'] = 'George'
Emily['ID'] = 'Emily'
Matt['ID'] = 'Matt'
Fozz['ID'] = 'Fozz'
Phil['ID'] = 'Phil'
Angelo['ID'] = 'Angelo'
Marco['ID'] = 'Marco'


df = pd.concat(players)

#Convert Team Value to string
df['TV'] = df['TV'].map(lambda x : float(x))
df['TV'] = df['TV'].map(lambda x : x[1:])
df['TV'] = df['TV'].map(lambda x : x.rstrip('m'))

print df.head(50)
