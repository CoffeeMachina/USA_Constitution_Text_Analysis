# random color generator
# https://xkcd.com/color/rgb.txt

import numpy as np
import pandas as pd
import re
df=pd.read_csv("xkcd_colors.txt")
df.columns = ['raw']
df['color']=df['raw'].apply(lambda x : x.split("\t")[0])
df['hex']=df['raw'].apply(lambda x : x.split("\t")[1])
df = df[['color','hex']]

def hex():
"""returns one random instance of HTML color code as a string"""
    return df.iloc[np.random.randint(1,948,1)].values[0][1]

def nhex(n=1):
"""returns pd.Series of random HTML color codes"""
    return df.iloc[np.random.randint(1,948,n)]['hex']


