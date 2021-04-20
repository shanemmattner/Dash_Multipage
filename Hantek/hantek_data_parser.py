# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 13:59:15 2021

@author: shane
"""

import numpy as np
import pandas as pd
import plotly.io as pio
import plotly.express as px
pio.renderers.default='browser'

SAMPLE_RATE = 1000000 # 1Mhz
SAMPLE_TIME = 1/SAMPLE_RATE
MEM_DEPTH = 130048 # TODO: read the text file and use the found value
TOTAL_TIME = 130048/1000000

df = pd.read_csv('data.txt', skiprows=5, delimiter = "\t")
df.columns=['CH1']
time = np.linspace(0, TOTAL_TIME,MEM_DEPTH-1)
# df.plot()

figln = px.line(df,x = time, y='CH1')
figln.show()  
