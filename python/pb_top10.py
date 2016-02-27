# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from getdata import *

PB_sort = df[['PB','ID']]

PB_sort = PB_sort.sort('PB', ascending=False)

PB_sort = PB_sort.rename(columns = {'PB':'Bench Points','ID':'Name'})

PB_sort_top = PB_sort.head(10)

PB_sort_top.to_html(open('PB_top10.html', 'w'))