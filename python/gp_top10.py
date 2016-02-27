# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from getdata import *

GP_sort = df[['GP','ID']]

GP_sort = GP_sort.sort('GP', ascending=False)

GP_sort = GP_sort.rename(columns = {'GP':'Gameweek Points','ID':'Name'})

GP_sort_top = GP_sort.head(10)

GP_sort_top.to_html(open('GP_top10.html', 'w'))